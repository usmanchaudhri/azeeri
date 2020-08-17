"""
Rotate the matrix in a spiral - from outer to inner spiral.
- rotate the four corners first in the outer spiral.
- increment to the next element in the outer spiral and rotate the corners again,
    keep repeating until the spiral is fully rotated.
- increment to the first inner spiral.
"""

def rotate90Clockwise(matrix):
    N = len(matrix[0])

    # an NxN matrix will have N//2 spirals to rotate
    for i in range(N//2):
        # for each inner spiral circle - which will be smaller - it will run N-i
        # for the outer most spiral i=0 to N=4
        # for the first inner spiral i=1 to N=4-1 => 3
        # for the second inner spiral i=2 to N=4-1 => 3
        for j in range(i, N-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N-1-j][i]
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
            matrix[N-1-i][N-1-j] = matrix[j][N-1-j]
            matrix[j][N-1-j] = temp

if __name__ == "__main__":
    matrix = [
        [ 1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]]
    print(5//2)