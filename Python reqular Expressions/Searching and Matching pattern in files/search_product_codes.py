import re , os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "Assets", "sample4.txt")

with open(file_path,"r") as f:
    text=f.read()

pattern=r'\b[A-Z]{2}\d{2}-[A-Z]{2}\d{2}\b|\b\d{3}-\d{3}\b'
matches=re.findall(pattern,text)

print("All Product Codes: ",matches)
