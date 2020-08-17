"""
tree

array[(i-1)/2]      - Returns the Parent node
array[(2*i)+1]      - Returns the left child node
array[(2*i)+2]      - Returns the right child node

Solution -
- since we have the list of array and the connected edges, we will build the a graph
- we would than need to traverse the graph using DFS traversal and when backtracking we
    need to than take the sum of sub-trees to than find the sum of the largest sub tree.

- [(1,2), (1,3), (2,6), (3,4), (3,5)]
"""
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V

        # create a dictionary where key is the parent vertex and list the adjacent vertex
        self.adjacent = defaultdict(list)

    def addEdge(self, vertex, adjVertex):
        # append adjVertex to vertex
        self.adjacent[vertex].append(adjVertex)
        print('')

    def dfs(self, s):
        # in dfs we need to track the visited vertex
        visited = [False for i in range(self.V)]

        # create a stack for dfs
        stack = []

        stack.append(s)
        while(stack):

            # pop a vertex from stack
            a = stack.pop()

            # check if the key exists in the dictionary
            if not visited[a]:
                visited[a] = True

                for node in self.adjacent[a]:
                    if not visited[node]:
                        stack.append(node)



if __name__ == "__main__":
    tree = [1, 2, 3, 4, 5, 6]
    g = Graph(len(tree))
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 6)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    # g.dfs(0)



