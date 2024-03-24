# books/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Book, Publisher
from .serializers import BookSerializer

class BooksByGenreList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Book.objects.filter(genre=genre)

class TopSellersList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by('-copies_sold')[:10]

class BooksByRatingList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        rating = self.kwargs['rating']
        return Book.objects.filter(rating__gte=rating)

class DiscountBooksByPublisher(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        discount_percent = request.data.get('discount_percent')
        publisher_name = request.data.get('publisher')

        if not (discount_percent and publisher_name):
            return Response({'error': 'Discount percent or publisher parameter is missing'}, status=400)

        try:
            discount_percent = float(discount_percent)
        except ValueError:
            return Response({'error': 'Invalid discount percent format'}, status=400)

        publisher, _ = Publisher.objects.get_or_create(name=publisher_name)
        books = Book.objects.filter(publisher=publisher)
        for book in books:
            book.price -= (book.price * discount_percent) / 100
            book.save()

        return Response({'message': 'Book prices updated successfully'})
