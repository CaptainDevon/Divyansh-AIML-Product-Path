import numpy as np

vector=np.array([1,2,3,4,5,6,7,8,9])

mask=vector>5

print("numbers greater than 5: ",vector[mask])