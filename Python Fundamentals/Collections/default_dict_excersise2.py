from collections import defaultdict

# Sample list of letters
letters=["a","b","a","c","b","a"]

letter_count=defaultdict(int)

for letter in letters:
    letter_count[letter]+=1

print(letter_count)