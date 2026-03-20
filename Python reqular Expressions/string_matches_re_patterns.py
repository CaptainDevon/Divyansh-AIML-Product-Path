import re

pattern=r'\d{4}-\d{2}-\d{2}'

date_string="2026-03-20"

match=re.fullmatch(pattern,date_string)

if match:
    print(f'the data string {date_string} is valid')

else:
    print(f'the data string {date_string} is invalid')
