
def rotate(matrix):
    if not len(matrix):
        return

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix) - 1

    while left < right and top < bottom:
        prev = matrix[top+1][left]

        # move elements of top row one step right
        for i in range(left, right+1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr

        # move elements of right most column one step downwards
        top += 1
        for i in range(top, bottom+1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr

        # move elements of bottom row to the left
        right -= 1
        for i in range(right, left-1, -1):
            curr = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = curr

        # move elements of left most column upwards
        bottom -= 1
        for i in range(bottom, top-1, -1):
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr

        left += 1

    return matrix


# def rotate(matrix):
#     length = len(matrix) - 1
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             temp = matrix[i][j]
#
#             matrix[i][j] = matrix[length-j][i]
#             matrix[length-j][i] = matrix[length-i][length-j]
#             matrix[length-i][length-j] = matrix[j][length-i]
#             matrix[length-j][i] = temp

if __name__  == "__main__":
    # [[6, 1, 2, 3, 4],
    #  [11, 12, 5, 7, 9],
    #  [16, 17, 8, 13, 15],
    #  [21, 18, 14, 19, 20],
    #  [22, 23, 24, 10, 25]]

    grid = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]]
    # rotate(grid)
    for i in range(len(grid)):
        rotate(grid)

        print(grid)

