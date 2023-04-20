from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to="media/video")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    book = models.FileField(upload_to="media/book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Presentation(models.Model):
    name = models.CharField(max_length=100)
    presentation = models.FileField(upload_to="media/pptx")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
