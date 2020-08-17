"""
Given N X N matrix filled with 1, 0, 2, 3. Find whether there is a path possible from source to destination, traversing
through blank cells only. You can traverse up, down, right and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
Note: there are an only a single source and single destination(sink).
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, source, destination):
        # base case
        if source == destination:
            return True

        # mark all nodes as False
        visited = [False] * (len(self.graph) + 1)

        # create a queue for BFS
        queue = []
        queue.append(source)

        while queue:

            # deque the queue
            source = queue.pop(0)

            # get all the adjacent vertices of the
            # dequed vertex
            for i in self.graph[source]:

                # if this adjacent node is the destination node,
                # than return True
                if i == destination:
                    return True

                # continue BFS
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        # If BFS is complete without visiting destination than the destination does not exits
        return False


def isSafe(i, j, matrix):
    if i >= 0 and i <= len(matrix) and j >= 0 and j <= len(matrix[0]):
        return True
    else:
        return False

def findPath(M):
    s, d = None, None # source and destination
    N = len(M)
    g = Graph()

    # create graph with n * n node
    # each cell consider as node
    k = 1 # Number of current vertex
    for i in range(N):
        for j in range(N):
            if (M[i][j] != 0):

                # connect all 4 adjacent cell to
                # current cell
                if (isSafe(i, j + 1, M)):
                    g.addEdge(k, k + 1)
                if (isSafe(i, j - 1, M)):
                    g.addEdge(k, k - 1)
                if (isSafe(i + 1, j, M)):
                    g.addEdge(k, k + N)
                if (isSafe(i - 1, j, M)):
                    g.addEdge(k, k - N)

            if (M[i][j] == 1):
                s = k

                # destination index
            if (M[i][j] == 2):
                d = k
            k += 1

    # find path Using BFS
    return g.BFS(s, d)

M =[[0, 3, 0, 1], [3, 0, 3, 3], [2, 3, 3, 3], [0, 3, 3, 3]]
if findPath(M):
    print("Yes")
else:
    print("No")

