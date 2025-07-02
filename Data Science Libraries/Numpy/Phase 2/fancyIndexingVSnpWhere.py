import numpy as np 
numbers=np.array([1,2,3,4,5,6,7,8,9])
indices=[0,2,4]
print(numbers[indices])


whereResult=np.where(numbers>5)
print(whereResult)
print(numbers[whereResult])