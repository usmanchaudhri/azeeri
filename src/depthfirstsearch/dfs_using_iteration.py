"""
"""
from collections import defaultdict

class Graph:
    def __init__(self, V):
        # total number of vertex in Graph
        self.V = V
        self.adjacent = defaultdict(list)

    def addEdge(self, vertex, adjVertex):
        # append adjVertex to the vertex
        self.adjacent[vertex].append(adjVertex)

    def dfs(self, s):
        # to track visited vertex, create array for number of vertices
        visited = [False for i in range(self.V)]

        # create a stack for DFS
        stack = []

        # push the current vertex to stack
        stack.append(s)
        while(len(stack)):

            # pop vertex from stack
            s = stack.pop()

            if(not visited[s]):
                print(s, end=' ')
                visited[s] = True

            # get all adjacent vertices of the vertex s
            # if a adjacent has not been visited, then push
            # it to the stack
            for node in self.adjacent[s]:
                if (not visited[node]):
                    stack.append(node)
                    print(stack)


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)

    g.dfs(0)




