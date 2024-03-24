from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    copies_sold = models.PositiveIntegerField()

    def __str__(self):
        return self.title
