import requests
from requests.auth import HTTPBasicAuth

username="username"
password="pass"

response=requests.get(
    "http://127.0.0.1:8000/protected",
    auth=HTTPBasicAuth(username=username,password=password)
)

print(response.text)