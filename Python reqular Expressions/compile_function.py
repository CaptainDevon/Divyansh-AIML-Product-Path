import re

pattern=r'\d+'
text='the price of the book is $19.99 and the price of the movie is $12.49'

regex=re.compile(pattern)
matches=regex.findall(text)
print(matches)