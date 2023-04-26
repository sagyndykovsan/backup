from django.db import models
from ckeditor.fields import RichTextField


class Scholarship(models.Model):
    name = models.CharField(max_length=150)
    header = models.CharField(max_length=150, blank=True)
    text = RichTextField(blank=True)
    image = models.ImageField(upload_to="stipendii_image", blank=True)
    detail_image = models.ImageField(upload_to="detail_image", blank=True)

    def __str__(self):
        return self.name
    
