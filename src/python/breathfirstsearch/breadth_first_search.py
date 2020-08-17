"""
In breadth first search we will visit all the adjacent node and will use a queue to keep track of the node.

Time complexity O (V + E) where V is the number of vertices and E is the edges
"""
def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        for neighbour in graph[s]:
            # visit all the adjacent nodes if they have not been visited already
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

bfs(graph, 'A')