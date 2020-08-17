from collections import defaultdict

class Graph:
    # sum = [1500  1300            1100     ]
    value = [100,  200,  100, 500, 100,  600]

    def __init__(self, noOfNodes):
        self.totalSum = sum(self.value)
        self.noOfNodes = noOfNodes
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # vertex is the index of the node
    def dfs(self, vertex):
        # what the max vertex's index is
        visited = [False] * (self.noOfNodes)
        self.dfsHelper(vertex, visited)

        res = list(map(lambda k: self.totalSum - k, self.value))
        return min(res)

    # vertex is the index of the node, we can get the value of that index from the value array
    def dfsHelper(self, vertex, visited):
        visited[vertex-1] = True

        # for each vertex in the adjacency list
        for i in self.graph[vertex]:
            if visited[i-1] == False:
                # during the backtracking we are finished traversing all the child nodes
                # of this sub tree.
                self.dfsHelper(i, visited)

                # vertex is the parent node and i is the adjacent child node
                # we will store the sum of each subtree at the parent level.
                # this way we can just subtract the total sum from each value in the array
                # and hence we can determine what the max diff in the array
                self.value[vertex-1] += self.value[i-1]


if __name__ == "__main__":

    tree = [1, 2, 3, 4, 5, 6]

    # the edges below are the indices of the vertex
    g = Graph(len(tree))
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)

    print(g.dfs(1))

    # value = [100, 200, 100, 500, 100, 600]
    # value = list(map(lambda k: 1500 - k, value))
    # print(value)

    # parsing 2d array
    # res = [[print(int(val)) for val in value] for value in array]
    # print(res)
    # array = [[1,2], [2,3]]
    # array = [2,3]
    # print(min(array))
    # print(array.pop())

