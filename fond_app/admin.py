from django.contrib import admin

from fond_app.models import Video, Book, Presentation, QA, Question

admin.site.register(Video)
admin.site.register(Book)
admin.site.register(Presentation)

admin.site.register(QA)
admin.site.register(Question)
