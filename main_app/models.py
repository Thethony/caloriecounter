from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Home(models.Model):
    pass