from collections import defaultdict

files=[
    ("reposr.docx","document"),
    ("summary.pdf","document"),
    ("budget.xlsx","spreadsheet"),
    ("data.csv","spreadsheet"),
    ("diagram.png","image")
]


# grouping by files

group_directory=defaultdict(list)

for filename,filetype in files:
    group_directory[filetype].append(filename)

print(dict(group_directory))