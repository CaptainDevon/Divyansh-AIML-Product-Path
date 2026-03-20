import re
pattern=r'the'

text='here are the sample of the regular expression in python'
match=re.search(pattern,text)
if match:
    print('Pattern Found')

else:
    print('Pattern not found')