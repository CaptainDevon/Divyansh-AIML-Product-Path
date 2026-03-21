import re
pattern=r'hello.*world'
text='hello\nworld'
match=re.search(pattern,text,re.DOTALL)

if match:
    print(f"Matched String: {match.group()}")
else:
    print("No match Group")