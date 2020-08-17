"""
    j1  j2  j3
j1  0,  0,  1
j2  1,  0,  1
j3  0,  0,  0

Consider the matrix as a graph where the column represents the node. So we have total of three nodes in this
Graph.
"""
def dfs_using_adjacency_matrix(matrix):
    visited = [False for i in range(len(matrix[0]))]

    # apply dfs for each each row
    priority = []
    for row in range(len(matrix)):
        jobs = dfs(row, matrix, visited)
        jobs.sort(reverse=True)
        priority = priority + jobs

    return priority

def dfs(row, matrix, visited):

    # parse each column and keep track of the nodes visited
    jobs = []
    stack = []
    stack.append(0)

    while len(stack):
        element = stack.pop()

        if not visited[element]:
            jobs.append(element)
            visited[element] = True

        # get all the adjacent vertices of row
        # and push it to the stack it not already visited.
        for j in range(1, len(matrix[0])):
            if matrix[row][j] == 1 and not visited[j]:
                stack.append(j)

    return jobs

matrix = [[0,0,1],
          [0,1,1],
          [0,0,0]]

print(dfs_using_adjacency_matrix(matrix))