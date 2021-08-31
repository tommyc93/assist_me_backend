from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Budget(models.Model):
    income = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=32)
    cost = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=1000, blank=True)

class Task(models.Model):
    name = models.CharField(max_length=500)
    time = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=1000, blank=True)
    due = models.DateField(null=True, blank=True)

class User(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    use = models.CharField(max_length=32)
