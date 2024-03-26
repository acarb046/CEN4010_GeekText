from django.urls import path
from .views import AuthorCreateView

urlpatterns = [
    path('author/', AuthorCreateView.as_view(), name='author-create'),
]
