from collections import defaultdict
dd=defaultdict(list)

dd['key1'].append(1)
print(dd['key2'])


dd=defaultdict(lambda:"Defaut value")
print(dd['key3'])