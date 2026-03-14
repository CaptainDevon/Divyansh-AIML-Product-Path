import requests

cookie={"user_id":"2"}
response=requests.get(
    "http://127.0.0.1:8000/api/cookies",
    cookies=cookie
)

print(response.cookies.get_dict())
print(response.cookies["user_id"])

print("===========================Request Headers=======================")
print(response.request.headers)

print("===========================Response Headers=======================")
print(response.headers)