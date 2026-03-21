import re

pattern=r'\b'
text=r'The quick \brown fox'
escaped_pattern=re.escape(pattern)
match=re.search(escaped_pattern,text)

if match:
    print('Found the word boundary in the text')

else:
    print('no word boundry found in the text')