import numpy as np 

vector=np.array([1,2,3,4,5,6,7,8,9])

print("basic slicing: ",vector[2:7])

# with step

print("With Stepping: ",vector[2:8:2])

# With negative indexing

print("Ngative Indexing: ", vector[8:2:-1])