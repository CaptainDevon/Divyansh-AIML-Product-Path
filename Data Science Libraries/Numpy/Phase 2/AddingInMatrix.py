import numpy as np 

matrix=np.array([[1,2,3],[4,5,6]])
newRow=np.array([7,8,9])

new_matrix=np.vstack((matrix,newRow))
print(new_matrix)

newCol=np.array([[11],[12],[13]])
newCol_matrix=np.hstack((new_matrix,newCol))
print(newCol_matrix)