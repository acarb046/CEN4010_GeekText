# books/urls.py
from django.urls import path
from .views import BooksByGenreList, TopSellersList, BooksByRatingList, DiscountBooksByPublisher

urlpatterns = [
    path('by_genre/<str:genre>/', BooksByGenreList.as_view(), name='books-by-genre'),
    path('top_sellers/', TopSellersList.as_view(), name='top-sellers'),
    path('by_rating/<str:rating>/', BooksByRatingList.as_view(), name='books-by-rating'),
    path('discount_books/', DiscountBooksByPublisher.as_view(), name='discount-books'),
]
