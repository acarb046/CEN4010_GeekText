from rest_framework import serializers

##
##

from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

from .models import ShoppingCart
class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

from .models import ShoppingCartItem
class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = '__all__'