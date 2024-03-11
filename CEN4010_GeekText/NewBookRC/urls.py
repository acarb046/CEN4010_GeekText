# NewBookRC/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router object
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'ratings-comments', views.RatingCommentViewSet)


# Define your app's URL patterns
urlpatterns = [
    # Include the URLs generated by the router
    path('', include(router.urls)),
]
