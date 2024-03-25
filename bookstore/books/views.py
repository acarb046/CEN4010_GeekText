from django.urls import path
from .views import get_books_by_genre, get_top_sellers, get_books_by_rating, update_book_prices

urlpatterns = [
    path('books/genre/', get_books_by_genre, name='books-by-genre'),
    path('books/top-sellers/', get_top_sellers, name='top-sellers'),
    path('books/rating/', get_books_by_rating, name='books-by-rating'),
    path('books/update-prices/', update_book_prices, name='update-book-prices'),
]
