import numpy as np 

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("specific element 2nd row 3rd column: ",matrix[1][2])

# we can also do like this 
print("specific element 2nd row 3rd column: ",matrix[1,2])

print("Specific row: ",matrix[1])
print("Specific Column: ",matrix[:,1])