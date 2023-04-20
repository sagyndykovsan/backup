from django.db import models


class Scholarship(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="media/stipendii_photo", blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
