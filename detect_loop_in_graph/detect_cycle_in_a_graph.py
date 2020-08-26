"""
detect cyccle in a graph
"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recursionStack):
        visited[v] = True
        recursionStack[v] = True

        for neighbors in self.graph[v]:
            # visit all the neighbours of the vertex v

            if visited[neighbors] == False:
                if self.isCyclicUtil(neighbors, visited, recursionStack) == True:
                    return True
            elif recursionStack[neighbors] == True:
                return True

        # the node needs to be popped from recursion stack
        # before function ends
        recursionStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recursionStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                # pass the current node, visited array, and the recursion stack
                self.isCyclicUtil(node, visited, recursionStack)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

if g.isCyclic() == 1:
    print('')
else:
    print('')





