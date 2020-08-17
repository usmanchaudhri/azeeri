"""
Given a sorted matrix where the number below and right of  you will always be bigger,
write an algorithm to find if a particular number exist in the matrix. What is the
running time of your algorithm.
"""

# O(n + m) time | O(1) space
# n is the length of rows and m is the length of columns
def searchInSortedMatrix(matrix, target):
    # pick top-right number in the matrix and compare it to the target number
    # depending on if the target is greater or equal to the number in matrix
    # we can either eliminate the entire row and move to the next row or the
    # entire column and move to the previous column

    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            # eliminate the whole column
            col -= 1
        elif matrix[row][col] < target:
            # eliminate the entire row
            row += 1
        else:
            return [row, col]

    return [-1, -1]


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41 , 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]

    target = 44
    searchInSortedMatrix(matrix, target)