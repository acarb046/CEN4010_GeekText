from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=255)
    year_published = models.IntegerField()
    copies_sold = models.IntegerField()
