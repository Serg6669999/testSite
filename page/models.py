from django.db import models


class Data(models.Model):
    number_1 = models.BigIntegerField()
    number_2 = models.BigIntegerField()


class User(models.Model):
    sender = models.EmailField()
    recipient = models.EmailField()
    password = models.SlugField()
    subject = models.CharField(max_length=200)
    text = models.TextField()
