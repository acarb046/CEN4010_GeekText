from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class GenreBookListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre')
        return Book.objects.filter(genre=genre)

class TopSellersListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by('-copies_sold')[:10]

class RatingBookListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        rating = float(self.request.query_params.get('rating'))
        return Book.objects.filter(rating__gte=rating)

class DiscountBooksByPublisherView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        discount_percent = float(request.data.get('discount_percent'))
        publisher = request.data.get('publisher')
        books = Book.objects.filter(publisher=publisher)
        for book in books:
            book.price -= book.price * (discount_percent / 100)
            book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
