import re
import os
file_extensions=['pdf','doc','docx','xls','xlsx','ppt','pptx']

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "Assets", "sample2.txt")

with open(file_path,"r") as f:
    text=f.read()
    pattern=r'\b\w+\.(?:' + '|'.join(file_extensions)+r')\b'
    matches=re.findall(pattern,text)

print(matches)