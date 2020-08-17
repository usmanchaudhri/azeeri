"""
depth first search
"""
def dfs(graph, node):
    visited = []
    stack = []

    stack.append(node)
    while stack:
        s = stack.pop()
        print(s, end=' ')

        # if s not in visited:
        #     visited.append(s)
        #     print(s, end=' ')

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

dfs(graph, 'A')