import re

pattern=r'\s+'
text='This is a sample text with multiple spaces'
word=re.split(pattern,text)
print(word)