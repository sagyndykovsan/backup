from django.contrib import admin

from contact.models import Contact, ContactMail, ContactPhone, ContactAddress

admin.site.register(Contact)
admin.site.register(ContactMail)
admin.site.register(ContactPhone)
admin.site.register(ContactAddress)