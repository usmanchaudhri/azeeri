"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands
"""

class Graph:
    def __init__(self, rows, cols, g):
        self.ROW = rows
        self.COL = cols
        self.graph = g

    def countIslands(self):
        # the main function which returns count of island
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # traverse through all cells
        # of a given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # if a cell with value 1 is not visited yet then a new island is found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # visit all cells in this island and increment island count
                    self.DFS(i, j, visited)
                    count +=1

    def DFS(self, i, j, visited):
        # check the 8 adjacent vertices
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

        # Mark this node visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                # [1][1]
                # check all surrounding cells
                # (1-1), (1-1) => (0)(0)
                # (1-1), (1+0) => (0)(1)
                # (1-1), (1+0) => (0)(1)
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)


    def isSafe(self, i, j, visited):
        # check if a given cell can be included in DFS
        return (i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j])


if __name__ == "__main__":
    graph =   [[1, 1, 0, 0, 0],
               [0, 1, 0, 0, 1],
               [1, 0, 0, 1, 1],
               [0, 0, 0, 0, 0],
               [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)
    g.countIslands()
