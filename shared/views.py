from django.shortcuts import render
from rest_framework import viewsets

##
##

from .models import User
from .serializers import UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from .models import Book
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

from .models import ShoppingCartItem
from .serializers import ShoppingCartItemSerializer
class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer