from django.shortcuts import render

from fond_app.models import Book, Presentation, Video
from scholarship.models import Scholarship


def index(request):
    el = Scholarship.objects.all()
    return render(request, "index.html", {"el": el})


def presentation(request):
    p = Presentation.objects.all()
    return render(request, "presentations.html", {"p": p})


def book(request):
    b = Book.objects.all()
    return render(request, "books.html", {"b": b})


def video(request):
    v = Video.objects.all()
    return render(request, "video.html", {"v": v})
