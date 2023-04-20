from django.db import models
from category.models import PostCategory


class Video(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=100, blank=True)
    video = models.FileField(upload_to="video", blank=True)
    image = models.ImageField(upload_to='video_image', blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=100, blank=True)
    book = models.FileField(upload_to="book", blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='book_image', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Presentation(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=100, blank=True)
    image = models.ImageField(upload_to='pptx_image', blank=True)
    presentation = models.FileField(upload_to="pptx", blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
