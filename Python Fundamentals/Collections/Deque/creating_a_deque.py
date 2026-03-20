from collections import deque

dq=deque()
print(dq)


dq1=deque((1,2,3)) #tuple
dq2=deque([4,5,6]) #list
dict={"a":1,"b":2,"c":3}
dq3=deque(dict.keys())
dq4=deque(dict.items())


print(dq1)
print(dq2)
print(dq3)
print(dq4)