import requests

response=requests.get("http://127.0.0.1:8000/api/items")


# If only wanna reveal the status code
print(response.status_code,end="\n\n")

# If only wanna reveal the content of the response 
print(response.content,end="\n\n")

# If only wanna reveal the text of the respone
print(response.text,end="\n\n")

# If only wanna reveal the headers of the response
print(response.headers,end="\n\n")

# If only wanna reveal the encoding of the response
print(response.encoding,end="\n\n")

# If only wanna reveal the cookies of the response
print(response.cookies,end="\n\n")

# If only wanna reveal the url 
print(response.url,end="\n\n")

# If Wanna see the response in the json format
print(response.json(),end="\n\n")
