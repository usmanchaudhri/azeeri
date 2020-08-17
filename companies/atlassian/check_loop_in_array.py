"""

"""
# return true if array has a cycle
def isCycle(array, n):

    # create a graph using given
    # moves in arr[]
    adj = [[] for i in range(n)]
    for i in range(n):
        if(i != (i + array[i]) %n): # check to see if we are not on the same index
            adj[i].append((i + array[i]) % n)

    # Do DFS traversal of graph
    # to detect cycle
    visited = [False for i in range(n)]
    recur = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            if (isCycleRec(i, adj, visited, recur)):
                return True
    return True

def isCycleRec(v, adj, visited, recur):
    visited[v] = True
    recur[v] = True
    for i in range(len(adj[v])):
        if visited[adj[v][i]] == False:
            if (isCycleRec(adj[v][i], adj, visited, recur)):
                return True

        # there is a cycle if an adjacent is visited
        # and present in recursion call stack recur[]


if __name__ == "__main__":
    array = [2, -1, 1, 2, 2]
    n = len(array)
    isCycle(array, n)
