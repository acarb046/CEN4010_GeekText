from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookCreateView(APIView):
    """
    An administrator must be able to create a book with the book ISBN,
    book name, book description, price, author,
    genre, publisher , year published and copies sold.
    * Logic: Given a Book’s info, add it to the system.
    * HTTP Request Type: POST
    * Parameters Sent: Book Object
    * Response Data: None
    """
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




