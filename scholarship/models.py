from django.db import models


class Scholarship(models.Model):
    name = models.CharField(max_length=150)
    header = models.CharField(max_length=150, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="stipendii_image", blank=True)

    def __str__(self):
        return self.name
