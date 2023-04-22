from django.db import models


class QA(models.Model):
    question = models.TextField()
    answer = models.TextField()


class Question(models.Model):
    name = models.CharField(max_length=50)
    question = models.TextField()
    subject = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
