from django.urls import path
from .views import BookDetailsAPIView

urlpatterns = [
    path('api/book/<str:isbn>/', BookDetailsAPIView.as_view(), name='book_details'),
]