from django.db import models

class Person(models.Model):
    forename = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
