from django.shortcuts import render, get_object_or_404
from news.models import News


def news(request):
    el = News.objects.all()
    return render(request, "news.html", {"el": el})

def detail_news(request):
    ds = News.objects.all()
    return render(request, "details_news.html", {"ds": ds})