import requests

response=requests.post(
    "http://127.0.0.1:8000/api/items",
    data={
        "name":"Gujiya",
        "price":100
    },
    allow_redirects=False
)

print(response.status_code)

print(response.request.body)
