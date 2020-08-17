"""
Once we find the cell we are interested in which has a '1'

The connectedCell method returns the largest connected graph size in the grid.
"""
# O(n*m) * n
def connectedCell(matrix):
    # return the size of the largest region
    ROWS = len(matrix)
    COLS = len(matrix[0])

    visited = [[False for col in range(COLS)] for row in range(ROWS)]
    largestConnectedGraph = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col] == False and matrix[row][col] == 1:
                size = find_connected_graph(matrix, visited, row, col)
                largestConnectedGraph = max(size, largestConnectedGraph)

    return largestConnectedGraph

# for the given (row, col) find all the connected points
def find_connected_graph(graph, visited, row, col):
    rowNbr = [-1,  0,  1, 1, 1, 0, -1, -1]
    colNbr = [-1, -1, -1, 0, 1, 1,  1,  0]

    visited[row][col] = True
    count = 1
    for k in range(8):
        if isSafe(graph, visited, row + rowNbr[k], col + colNbr[k]):
            count += find_connected_graph(graph, visited, row + rowNbr[k], col + colNbr[k])
    return count

def isSafe(graph, visited, row, col):
    return (row >= 0 and row < len(graph) and col >= 0 and col < len(graph[0])
            and not visited[row][col] and graph[row][col] == 1)


if __name__ == "__main__":
    matrix = [[1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 0],
              [1, 0, 0, 0]]
    print(connectedCell(matrix))

