import os
import requests

base_directory=os.path.dirname(__file__)
print(base_directory)

with open(os.path.join(base_directory,"sample_text1.txt"),"rb") as f1, open(os.path.join(base_directory,"sample_text2.txt"),"rb") as f2:
    files=[
        ("files",("sample_text1.txt",f1,"text/plain")),
        ("files",("sample_text2.txt",f2,"text/plain"))
    ]

    response=requests.post("http://127.0.0.1:8000/uppload-files",files=files)
    print(response.json())