import requests

# Giving Wrong credentials
wrong_credentials ={
    "username":"Lalalalla",
    "password":"dnsjdndj"
}


# Giving Correct Credentials
right_credentials={
    "username":"some_name",
    "password":"pass"
}


deny_authentication=requests.post(
    "http://127.0.0.1:8000/api/login",
    data=wrong_credentials
)

accept_authentication=requests.post(
    "http://127.0.0.1:8000/api/items",
    data=right_credentials
)


# Cookie Creation
wrong_cookies=deny_authentication.cookies
print(f"Cookies returned from login: {wrong_cookies.get_dict()}")
print(f"Login response: {wrong_cookies.text}")

right_cookies=deny_authentication.cookies
print(f"Cookies returned from login: {right_cookies.get_dict()}")
print(f"Login response: {right_cookies.text}")

# Using Cookie to Access The Protected endpoint
wrong_response=requests.get(
    "http://127.0.0.1:8000/protected",
    cookies=wrong_cookies
)

print("Protected Route: ")
print(f"protected endpoint response: {wrong_response.text}")
print(wrong_response)


right_response=requests.get(
    "http://127.0.0.1:8000/protected",
    cookies=right_cookies
)

print("Protected Route: ")
print(f"protected endpoint response: {right_response.text}")
print(right_response)

