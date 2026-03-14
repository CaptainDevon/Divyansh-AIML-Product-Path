import requests

response=requests.get("http://127.0.0.1:8000/api/items")

print(response.json()[3]['price'])

print(response.json()[5]['name'])