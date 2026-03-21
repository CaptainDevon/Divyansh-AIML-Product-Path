import re
import os

phone_pattern=r'\d{3}-\d{3}-\d{4}'
email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
zip_pattern=r'\b\d{5}(?:-\d{4})?\b'
order_pattern=r'b[A-Z]{2}-\d{4}-\d{4}\b'
hex_pattern=r'#[A-Fa-f0-9]{6}'

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "Assets", "sample3.txt")

with open(file_path,"r") as f:
    text=f.read()
    phone_match=re.search(phone_pattern,text)
    email_match=re.search(email_pattern,text)
    zip_match=re.search(zip_pattern,text)
    order_match=re.search(order_pattern,text)
    hex_match=re.search(hex_pattern,text)

if phone_match:
    print('Phone number found :',phone_match.group())
if email_match:
    print('email id found :',email_match.group())
if zip_match:
    print('zip found :',zip_match.group())
if order_match:
    print('order number found :',order_match.group())
if hex_match:
    print('hex code found :',hex_match.group())