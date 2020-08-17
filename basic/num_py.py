import numpy as np

def split_array(array):
    array = np.array(array)
    array_split = np.array_split(array, 4)

    print(type(array_split))
    print(array_split[2])
    print(len(array_split))

def createNumpyOneDimensionalArray():
    my_list = [1,2,3,4,5,6]
    numpy_list = np.array(my_list)
    print(numpy_list)

def createNumpyTwoDimensionalArray():
    my_list = [[1,2,3], [4,5,6], [7,8,9]]
    numpy_list = np.array(my_list)
    print(numpy_list)

def expand_dimensions():
    my_list = [1,2,3,4,5,6]
    print(my_list)
    numpy_list = np.expand_dims(my_list, axis=1)
    print(numpy_list)
    print(numpy_list[0][0])

def createNparrayUsingArrange():
    print(np.arange(10))
    print(np.arange(0, 10))
    print(np.arange(0, 11, 2))
    print(np.zeros(7))
    print(np.ones(5))
    print(np.zeros((3, 5)))
    print(np.linspace(1, 3, 15))

def createIdentityMatrixInNumpy():
    my_matrix = np.eye(6)
    print(type(my_matrix[3][1]))

def randonNumberArray():
    nums = np.random.rand(25, 9)
    print(nums)
    print(nums.reshape(5, 5))
    print('max number %s', nums.max())
    print('min number %s', nums,min())
    print('max index in the array %s', nums.argmax())
    print('min index in the array %s', nums.argmin())

def shape():
    nums = np.random.rand(25, 10)
    print(nums.shape)

def reshape():
    mat = np.arange(1,26)
    print(mat)
    print(mat.reshape(5,5))

def indexNumpy():
    my_array = np.arange(0,11)
    print(my_array[8])

def arrayTwoD():
    two_d_arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
    print(two_d_arr[0, 1])

def conditionalStatements():
    new_arr = np.arange(5,15)
    print(new_arr)
    print(new_arr[new_arr > 10])
    print(new_arr[(new_arr > 6) & (new_arr < 10)])
    # print(new_arr > 10)

def broadcasting():
    my_array = np.arange(5,15)
    my_array[0:3] = 50
    print(my_array)

def sumElementsInNumpy():
    mat = np.arange(1,26).reshape(5,5)
    print(mat.sum())         #Returns the sum of all the values in mat
    print(mat.sum(axis=0))   #Returns the sum of all the columns in mat
    print(mat.sum(axis=1))   #Returns the sum of all the rows in mat

def axis():
    my_list = [[1,2,3],[4,5,6]]
    numpy_list = np.array(my_list)
    print('columns wise', numpy_list.sum(axis=0).shape)
    print('row wise', numpy_list.sum(axis=1).shape)

def squeeze():
    numpy_list = np.array([[1,2,3],[4,5,6]])
    print(numpy_list.shape)
    print(numpy_list.squeeze(axis=1))



if __name__ == "__main__":
    # createNumpyOneDimensionalArray()
    # createNumpyTwoDimensionalArray()
    # expand_dimensions()
    # createNparrayUsingArrange()
    # createIdentityMatrixInNumpy()
    # randonNumberArray()
    # shape()
    # arrayTwoD()
    # conditionalStatements()
    # broadcasting()
    # reshape()
    # sumElementsInNumpy()
    # axis()
    # squeeze()
    # loopOverTuple()
    expand_dimensions()