import numpy as np 
import time 

startList=time.time()
py_list=[i*2 for i in range(1000000)]
print("\n List Operation Time: ", time.time()-startList)


startArray=time.time()
np_array=np.arange(1000000)*2
print("\n npArray Operation Time: ", time.time()-startArray)