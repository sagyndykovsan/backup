from django.db import models
from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


class EventType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    link = models.URLField(max_length=200)
    type = models.ManyToManyField(EventType)

    def clean(self):
        if self.start_datetime and self.end_datetime:
            if self.start_datetime > self.end_datetime:
                raise ValidationError(_('End datetime must be greater than or equal to start datetime.'))

    def save(self, *args, **kwargs):
        self.clean()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.start_datetime} - {self.end_datetime})'

