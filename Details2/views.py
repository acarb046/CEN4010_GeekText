from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookDetailsAPIView(APIView):
    def get(self, request, isbn):
        try:
            book = Book.objects.get(isbn=isbn)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


from django.shortcuts import render

# Create your views here.
