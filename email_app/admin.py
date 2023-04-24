from django.contrib import admin
from .models import ContactEmail

# Register your models here.


@admin.register(ContactEmail)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
