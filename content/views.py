from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article


def content_list(request):

    q = request.GET.get("q")

    all_content = Article.objects.all()

    content = all_content

    if q:
        content = content.filter(title__icontains=q)

    paginator = Paginator(content, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    featured = page_obj.object_list[0] if page_obj.object_list else None
    others = page_obj.object_list[1:] if page_obj.object_list else []

    return render(request, "content/list.html", {
        "featured": featured,
        "content": others,
        "page_obj": page_obj,
        "q": q,
        "latest_content": all_content[:5],
    })


def content_detail(request, pk):
    item = get_object_or_404(Article, pk=pk)

    return render(request, "content/detail.html", {
        "item": item
    })