from django.urls import path
from . import views
from .views import my_view, get_wishlist
from django.shortcuts import redirect

urlpatterns = [
    path('user/<int:user_id>/wishlist/', views.get_user_wishlist,name='get_user_wishlist'),
    path('wishlist_items/', views.get_wishlist_items, name='wishlist_items'),
    path('get_wishlist/<int:user_id>/', views.get_wishlist, name='get_wishlist'),
    path('my_view/', views.my_view, name='my_view'),  # Adjusted to use views.my_view
    path('', lambda request: redirect('user/1/wishlist', permanent=False)),  # Correct syntax for redirect
]

