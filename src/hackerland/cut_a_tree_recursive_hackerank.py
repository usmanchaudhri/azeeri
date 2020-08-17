#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
from collections import defaultdict

class Graph:
    def __init__(self, totalNodes, value):
        self.totalNodes = totalNodes
        self.value = value
        self.graph = defaultdict(list)
        self.totalSum = sum(value)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex):
        visited = [False] * (self.totalNodes)
        self.helper(vertex, visited)

        res = list(map(lambda k: self.totalSum - k, self.value))
        return min(res)

    def helper(self, vertex, visited):
        visited[vertex-1] = True
        for i in self.graph[vertex]:
            if visited[i-1] == False:
                self.helper(i, visited)

                self.value[vertex-1] += self.value[i-1]

def cutTheTree(data, edges):
    # Write your code here
    g = Graph(len(data), data)
    for edge in edges:
        g.addEdge(edge[0], edge[1])

    g.dfs(edges[0][0])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

