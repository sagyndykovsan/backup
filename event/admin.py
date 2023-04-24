from django.contrib import admin

from event.models import Event, EventType


admin.site.register(Event)
admin.site.register(EventType)
# Register your models here.
