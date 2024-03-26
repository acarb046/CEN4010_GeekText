from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

##
##

from .views import UserViewSet
router.register(r'users', UserViewSet)

from .views import BookViewSet
router.register(r'books', BookViewSet)

from .views import ShoppingCartViewSet
router.register(r'shopping-carts', ShoppingCartViewSet)

from .views import ShoppingCartItemViewSet
router.register(r'shopping-cart-items', ShoppingCartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]