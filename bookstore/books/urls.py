from django.urls import path
from .views import GenreBookListView, TopSellersListView, RatingBookListView, DiscountBooksByPublisherView


urlpatterns = [
    path('home/', views.home, name='home'),  # Example URL pattern
    # Define more URL patterns as needed
    path('genre-books/', GenreBookListView.as_view(), name='genre-books'),
    path('top-sellers/', TopSellersListView.as_view(), name='top-sellers'),
    path('rating-books/', RatingBookListView.as_view(), name='rating-books'),
    path('discount-books/', DiscountBooksByPublisherView.as_view(), name='discount-books'),
]
