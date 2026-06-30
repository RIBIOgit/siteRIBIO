from django.shortcuts import render
from news.models import News

def home(request):
    latest_news = News.objects.all()[:3]

    return render(request, "portal/home.html", {
        "latest_news": latest_news
    })