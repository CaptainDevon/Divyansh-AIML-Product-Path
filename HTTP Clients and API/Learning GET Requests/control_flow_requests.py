import requests

response1=requests.get("http://127.0.0.1:8000/api/items")
response2=requests.get("http://127.0.0.1:800/api/illustrations")

def print_server_response(response):
    if response.status_code==200:
        print("congratulations you have hit the API!")

    elif response.status_code==404:
        print("Sorry, The requested endpoint doesnt exist")

    else:
        print("Internal Server error")


if __name__=="__main__":
    print_server_response(response1)
    print_server_response(response2)