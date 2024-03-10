from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserProfile

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        name = data.get('name', '')
        email = data.get('email', '')
        home_address = data.get('home_address', '')

        # Create the user profile
        UserProfile.objects.create(
            username=username,
            password=password,
            name=name,
            email=email,
            home_address=home_address
        )

        return JsonResponse({'message': 'User created successfully'}, status=201)
    else:
        #return JsonResponse({'error': 'Method not allowed'}, status=405)
        return JsonResponse({'Success!': 'User 101 is here'}, status=405)

def get_dummy_profile_data(request):
    # Retrieve all dummy user profiles from the database
    dummy_profiles = UserProfile.objects.all()

    # Serialize the data into JSON format
    serialized_profiles = [
        {
            'username': profile.username,
            'name': profile.name,
            'email': profile.email,
            'home_address': profile.home_address
        }
        for profile in dummy_profiles
    ]

    # Return the serialized data as a JSON response
    return JsonResponse({'dummy_profiles': serialized_profiles})