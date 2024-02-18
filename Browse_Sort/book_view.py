# books/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def books_by_genre(request, genre):
    books = Book.objects.filter(genre=genre)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
