from django.db import models


class Contact(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class ContactMail(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class ContactPhone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class ContactAddress(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Contact address"
        verbose_name_plural = "Contact address"

    def __str__(self):
        return self.address


