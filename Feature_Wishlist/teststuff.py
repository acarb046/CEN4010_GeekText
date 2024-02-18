import requests

url = 'http://http://127.0.0.1:8000/wishlist/1/'

response = requests.get(url)

if response.status_code == 200:

    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.reason}")
