import re

pattern=r'\d+'
text='Hello my name is Divyansh Sinha i was born in 9th january i am Software Developer having currently 9 months of experience'
matches=re.findall(pattern,text)
print(matches)