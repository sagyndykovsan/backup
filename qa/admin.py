from django.contrib import admin

# Register your models here.
from qa.models import QA, Question

admin.site.register(QA)
admin.site.register(Question)