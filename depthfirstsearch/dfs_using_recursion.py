from collections import defaultdict

class Graph:

    def __init__(self):
        # each value in the dict is an edge
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex):
        # mark all the vertices as not visited
        visited = [False for i in range(len(self.graph))]
        print(visited)
        self.dfsUtil(vertex, visited)

    def dfsUtil(self, vertex, visited):
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                self.dfsUtil(i, visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(4, 5)
    g.addEdge(4, 6)

    g.dfs(2)