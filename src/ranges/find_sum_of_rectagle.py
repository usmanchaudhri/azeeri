"""
Range Sum Query 2D - Immutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
(row1, col1) and lower right corner (row2, col2).
"""

def preProcess_1_test():
    array = [[1, 2, 0, 3, 4, 1, 5, 8, 1, 0],
        [1, 5, 5, 2, 4, 9, 1, 2, 0, 1],
        [3, 8, 1, 3, 3, 7, 2, 1, 4, 9],
        [5, 2, 8, 6, 1, 0, 8, 4, 2, 3],
        [1, 4, 2, 5, 6, 3, 0, 1, 8, 1],
        [8, 2, 3, 5, 4, 1, 7, 2, 9, 3],
        [1, 7, 1, 0, 0, 1, 2, 7, 4, 3],
        [8, 5, 5, 9, 1, 2, 0, 3, 4, 2]]

    # initialize the sumArray
    rows = len(array)
    cols = len(array[0])
    sumArray = [[0 for i in range(cols)] for i in range(rows)]

    # make sure the sums matrix has the correct dimensions as well
    assert ('mismatching number of rows in the sumArray') / len(sumArray) == rows
    assert ('mismatching number of columns in the sumArray') / len(sumArray[0]) == cols

    preProcess(array, sumArray)

def preProcess(array, sumArray):
    # Copy first row of array[][] to sumArray
    for i in range(0, len(array[0]), 1):
        sumArray[0][i] = array[0][i]

    # Traverse the matrix and calculate the column wise sum
    # In the inner loop the row will increment and column will remain the same for sumArray[i-1][j]
    #[[1, 2, 3]
    #  |  |  |
    # [4, 5, 6]
    #  |  |  |
    # [7, 8, 9]]
    for i in range(1, len(array), 1):
        for j in range(0, len(array[0]), 1):
            sumArray[i][j] = array[i][j] + sumArray[i-1][j]
            # sumArray[1][0] = array[1][0] + sumArray[1-1][0] => sumArray[1][0] = array[1][0] + sumArray[0][0]
            # sumArray[1][1] = array[1][1] + sumArray[1-1][1] => sumArray[1][1] = array[1][1] + sumArray[0][1]
            # sumArray[1][2] = array[1][2] + sumArray[1-1][2] => sumArray[1][2] = array[1][2] + sumArray[0][2]
            # sumArray[1][3] = array[1][3] + sumArray[1-1][3] => sumArray[1][3] = array[1][3] + sumArray[0][3]

            # sumArray[2][0] = array[2][0] + sumArray[2-1][0] => sumArray[2][0] = array[2][0] + sumArray[1][0]
            # sumArray[2][1] = array[2][1] + sumArray[2-1][1] => sumArray[2][1] = array[2][1] + sumArray[1][1]
            # sumArray[2][2] = array[2][2] + sumArray[2-1][2] => sumArray[2][2] = array[2][2] + sumArray[1][2]
            # sumArray[2][3] = array[2][3] + sumArray[2-1][3] => sumArray[2][3] = array[2][3] + sumArray[1][3]

    # Traverse the matrix and calculate the row wise sum
    # In the inner loop the row will remain the same and column will be incremented for sumArray[i][j-1]
    #[[1 -> 2 -> 3]
    # [4 -> 5 -> 6]
    # [7 -> 8 -> 9]]
    for i in range(0, len(array), 1):
        sum = 0
        for j in range(0, len(array[0]), 1):
            sum = sum + sumArray[i][j]
            sumArray[i][j] = sum

def sumOfRectangle(array, startX, startY, endX, endY):
    # result is not sum of elements between
    # (0, 0) and (endX, endY)
    # this is calculating the sum of the larger matrix
    res = array[endX][endY]

    # remove elements between (0, 0) and (startX-1, endY)
    if startX > 0 and startX < len(array[0]):
        res = res - array[startX -1][endY]

    # remove elements between (0, 0) and (endX, startY-1)
    if startY > 0 and startY < len(array):
        res = res - array[endX][startY-1]

    # add elements between (0, 0) and (startX-1, startY-1)
    # since this section of the matrix was subtracted
    # twice in the above operation
    if startX > 0 and startY > 0:
        res = res + array[startX-1][startY-1]

    return res

if __name__ == "__main__":
    array = [[3, 0, 1, 4, 2],
             [5, 6, 3, 2, 1],
             [1, 2, 0, 1, 5],
             [4, 1, 0, 1, 7],
             [1, 0, 3, 0, 5]]

    # initialize the sumArray
    rows = len(array)
    cols = len(array[0])
    sumArray = [[0 for i in range(rows)] for i in range(cols)]
    preProcess(array, sumArray)
    result = sumOfRectangle(sumArray, 1, 1, 4, 4)
    print(result)
