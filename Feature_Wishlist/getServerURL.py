from django.http import HttpRequest
from django.http import JsonResponse


def get_base_url(request: HttpRequest) -> str:
    # Get the protocol (http or https) from the request
    protocol = request.scheme

    # Get the host (domain) from the request
    host = request.get_host()

    # Construct the base URL by combining the protocol and host
    base_url = f"{protocol}://{host}"

    return base_url


def my_view(request):
    # Get the base URL dynamically
    base_url = get_base_url(request)

    return JsonResponse({'base_url': base_url})