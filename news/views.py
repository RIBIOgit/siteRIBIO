from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News

def news_list(request):
    q = request.GET.get("q")

    # 🧠 base completa (para sidebar)
    all_news = News.objects.all()

    # 🔍 lista principal (filtrada)
    news_list = all_news
    if q:
        news_list = news_list.filter(title__icontains=q)

    paginator = Paginator(news_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    featured = page_obj.object_list[0] if page_obj.object_list else None
    others = page_obj.object_list[1:] if page_obj.object_list else []

    return render(request, "news/list.html", {
        "featured": featured,
        "news": others,
        "page_obj": page_obj,
        "q": q,
        "latest_news": all_news[:5]   # 👈 ISSO AQUI É O IMPORTANTE
    })

# 📰 DETALHE (artigo completo)
def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk)

    return render(request, "news/detail.html", {
        "item": item
    })