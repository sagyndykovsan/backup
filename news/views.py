from django.shortcuts import render, get_object_or_404
from news.models import News


def news(request):
    el = News.objects.all()
    return render(request, "news.html", {"el": el})


# def detail(request):
#     d = News.objects.all()
#     return render(request, "details.html", {"d": d})