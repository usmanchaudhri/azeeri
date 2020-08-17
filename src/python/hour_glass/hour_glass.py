"""

"""
def hour_glass(matrix):
    # starting from 1st row and 1st column
    print('rows', len(matrix))
    print('cols', len(matrix[0]))

    allSums = []
    for row in range(1, len(matrix)-1):
        for col in range(1, len(matrix[0])-1):
            currSum = hour_glass_sum(row, col, matrix)
            allSums.append(currSum)

    # print('All hour glasses', allSums)
    allSums.sort()
    return allSums[0]

def hour_glass_sum(row, col, matrix):
    rowIdx = [-1, -1, -1,  1, 1, 1]
    colIdx = [-1,  0,  1, -1, 0, 1]

    # traverse in hour glass and generate the sum
    currSum = matrix[row][col]
    for k in range(6):
        if row > 0 and row < len(matrix) and col > 0 and col < len(matrix[0]):
            currSum += matrix[row + rowIdx[k]][col + colIdx[k]]
    return currSum

if __name__ == "__main__":
    arr = [ [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

    hour_glass(arr)

    # for i in range(5):
    #     print(i)