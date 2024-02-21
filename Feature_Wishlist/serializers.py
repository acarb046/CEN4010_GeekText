from rest_framework import serializers
from .models import Wishlistitems, Books, Wishlist


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class WishlistItemSerializer(serializers.ModelSerializer):
    bookid = BooksSerializer(read_only=True)

    class Meta:
        model = Wishlistitems
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = '__all__'

