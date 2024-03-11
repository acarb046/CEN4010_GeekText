# models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)



class RatingComment(models.Model):
    rating_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    comment_date = models.DateField()

    def __str__(self):
        return f"Rating ID: {self.rating_id}, Book ID: {self.book_id}, User ID: {self.user_id}, Rating: {self.rating}, Comment: {self.comment}, Comment Date: {self.comment_date}"
