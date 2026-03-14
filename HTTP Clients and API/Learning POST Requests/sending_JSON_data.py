import requests

form_data={
    "name":"Chicken Shawarma Pizza",
    "price":476
}

response=requests.post(
    "http://127.0.0.1:8000/api/items",
    json=form_data
)

print(response.json())
print(response.status_code)