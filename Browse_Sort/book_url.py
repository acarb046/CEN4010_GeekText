# books/urls.py
from django.urls import path
from views import books_by_genre

urlpatterns = [
    path('books/by_genre/<str:genre>/', books_by_genre, name='books_by_genre'),
]

