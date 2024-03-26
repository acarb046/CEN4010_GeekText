from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    publisher = models.CharField(max_length=100)


auth_permission