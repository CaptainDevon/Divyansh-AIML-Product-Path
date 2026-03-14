import requests

response=requests.get("http://127.0.0.1:8000/api/items?offset=2&limit=2&max_price=40")

print(response.json())