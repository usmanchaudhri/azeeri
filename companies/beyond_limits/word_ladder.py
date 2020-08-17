"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        # create a dictionary where key is the parent vertex and list the adjacent vertex
        self.adjacent = defaultdict(list)

    def addEdge(self, vertex, adj_vertex):
        self.adjacent[vertex].append(adj_vertex)

    def __repr__(self):
        pass

def build_graph(begin_word, end_word, words):
    d = defaultdict(list)
    g = Graph()

    # create bucket of words that differ by one letter
    for word in words:
        for i in range(len(word)):
            # this create word buckets using blank spaces at different locations
            bucket = word[:i] + '_' + word[i+1:]
            d[bucket].append(word)

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def bfs(begin_word, end_word, graph):
    queue = []
    visited = []

    queue.append(begin_word)
    while queue:
        curr_word = queue.pop(0)
        print(curr_word, end=' ')

        if curr_word == end_word:
            break

        # find the neighbor
        for neighbor_word in graph[curr_word]:
            if neighbor_word not in visited:
                visited.append(neighbor_word)
                queue.append(neighbor_word)

    print(curr_word)

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
graph = build_graph(beginWord, endWord, wordList)
print(graph.adjacent)
bfs('hit', 'cog', graph)

