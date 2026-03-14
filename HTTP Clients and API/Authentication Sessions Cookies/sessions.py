import requests

with requests.Session() as session:
    credentials={
        "username":"some_name",
        "password":"pass"
    }

    login_response=session.post("http://127.0.0.1:8000/api/login",data=credentials)


    print("Cookies returned from the login: ")
    print(session.cookies.get_dict())
    print("Response from login: ")
    print(login_response.text)

    response=session.get("http://127.0.0.1:8000/protected")

    print("Protected Route: ")
    print(response.status_code)
    print(response.text)
    