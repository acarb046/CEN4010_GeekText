from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    home_address = models.TextField(blank=True)