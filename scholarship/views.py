from django.shortcuts import render, get_object_or_404
from scholarship.models import Scholarship


def scholarship(request):
    el = Scholarship.objects.all()
    return render(request, "project.html", {"el": el})

def detail(request):
    d = Scholarship.objects.all()


def scholarship_name(request):
    names = Scholarship.objects.all()
    return render(request, "details.html", {"names": names})


def detail(request, pk):
    d = Scholarship.objects.get(pk=pk)
    return render(request, "details.html", {"d": d})
