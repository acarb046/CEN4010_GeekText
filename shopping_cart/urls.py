from django.urls import path
from . import views

urlpatterns = [
    path('get-book-price/<int:book_id>/', views.get_book_price, name='get_book_price'),
    # ... other patterns
]