from rest_framework import serializers
from .models import Book, RatingComment

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # This will include all fields from the RatingComment model
class RatingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingComment
        fields = '__all__'  # This will include all fields from the RatingComment model
