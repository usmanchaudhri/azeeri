import numpy as np

# expand one
array = [1,2,3,4,5,6,7]
array_res = np.expand_dims(array, axis=1)
print(array_res)