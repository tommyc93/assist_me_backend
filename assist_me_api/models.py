from django.db import models

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=32)
    cost = models.IntegerField(null=True)
    note = models.CharField(max_length=400, blank=True)

class Expense(models.Model):
    name = models.CharField(max_length=32)
    cost = models.IntegerField(null=True)
    note = models.CharField(max_length=400, blank=True)

class Task(models.Model):
    name = models.CharField(max_length=32)
    time = models.IntegerField(null=True)
    note = models.CharField(max_length=400, blank=True)

class Daily(models.Model):
    name = models.CharField(max_length=32)
    time = models.IntegerField(null=True)
    note = models.CharField(max_length=400, blank=True)
    due = models.DateField(null=True)

class User(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=500)
