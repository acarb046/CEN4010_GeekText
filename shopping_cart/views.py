from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from shared.models import Book
from django.core.exceptions import ObjectDoesNotExist

def get_book_price(request, book_id):
    try:
        book = get_object_or_404(Book, id=book_id)
        payload = {
            'price': book.price
        }

        return JsonResponse(payload)
    
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Book not found with given ID.'}, status=404)