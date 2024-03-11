# NewBookRC/views.py

from rest_framework import viewsets
from .models import Book, RatingComment
from .serializers import BookSerializer, RatingCommentSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RatingCommentViewSet(viewsets.ModelViewSet):
    queryset = RatingComment.objects.all()
    serializer_class = RatingCommentSerializer
