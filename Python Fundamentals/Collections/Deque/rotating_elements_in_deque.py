from collections import deque

letters=deque(['a','b','c'])
print(letters)

letters.rotate()
print(letters)
letters.rotate(2)
print(letters)
letters.rotate(-1)
print(letters)