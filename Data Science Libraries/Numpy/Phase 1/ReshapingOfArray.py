import numpy as np 

vector=np.arange(12)
print("Original Array: ",vector)

reshaped=vector.reshape((2,6))

print("Reshaped Array: ",reshaped)

flattArray=reshaped.flatten()
print("Flattend Array: ",flattArray)

raveled=reshaped.ravel()  # Returns the copy of the original array
print("Raveled Array: ",raveled)

