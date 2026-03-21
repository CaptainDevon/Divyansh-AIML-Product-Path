import re
text="Hello my name is Divyansh Sinha I am working as a software developer at an MNC"

substring="software"

match=re.search(substring,text)

if match:
    print(f"Substring found at index: {match.start()}")

else:
    print(f"Substring not found in the text")