from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BooksViewset)
router.register(r'Wishlist', views.WishlistViewset)
router.register(r'WishlistItems', views.WishlistItemViewset)

urlpatterns = [
    path('', include(router.urls)),
]