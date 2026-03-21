import re 

pattern=r'hello'
text='Hello World'
match=re.search(pattern,text,re.IGNORECASE)

if match:
    print(f"Matched String: {match.group()}")
else:
    print("No match Group")