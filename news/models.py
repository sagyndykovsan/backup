import datetime
from django.db import models
from category.models import PostCategory

class News(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    preview = models.ImageField(upload_to='news_image')
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name
    