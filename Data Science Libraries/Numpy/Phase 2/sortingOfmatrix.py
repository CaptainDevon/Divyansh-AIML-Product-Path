import numpy as np 
matrix=np.array([[8,9,7],[6,1,3],[4,2,0]])

print("Unsorted Matrix: ",matrix)
print("Sorted Matrix row wise: ",np.sort(matrix,axis=1)) 
print("Sorted Matrix Column wise: ",np.sort(matrix,axis=0))
