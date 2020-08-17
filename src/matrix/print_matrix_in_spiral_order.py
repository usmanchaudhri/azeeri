"""
Given a M*N matrix, print matrix in a spiral order

Image the matrix as concentric circles i.e. the outer most circle and inner circles. The four corners being four for
loops which will increment and print the values as it rotates. Once the four loops reach the end of
rows or end of columns it will than increment to the inner cirlce.

input:
[[ 1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]]

output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
"""

def printSpiralOrder(matrix):
    top = 0
    left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    while True:

        if left > right: break
        for i in range(left, right+1, 1):
            print(matrix[top][i])
        top +=1

        if top > bottom: break
        for i in range(top, bottom+1, 1):
            print(matrix[i][right])
        right -=1

        if left > right: break
        for i in range(right, left-1, -1):
            print(matrix[bottom][i])
        bottom -=1

        if top > bottom: break
        for i in range(bottom, top-1, -1):
            print(matrix[i][left])
        left +=1

if __name__ == "__main__":

    # output:
    matrix = [
        [ 1, 2, 3, 4, 5],
         [16, 17, 18, 19, 6],
         [15, 24, 25, 20, 7],
         [14, 23, 22, 21, 8],
         [13, 12, 11, 10, 9]]
    printSpiralOrder(matrix)