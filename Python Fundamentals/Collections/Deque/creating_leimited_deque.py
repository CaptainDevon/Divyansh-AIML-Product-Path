from collections import deque

numbers=deque([0,1,2,3],maxlen=5)

print("Maxlen: ",numbers.maxlen)

numbers.appendleft(-1)
print(numbers)
numbers.append(5)
print(numbers)
numbers.appendleft(4)
print(numbers)