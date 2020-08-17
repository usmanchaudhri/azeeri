from python.find_word_on_a_board.sufix_tree import SuffixTrie
from collections import defaultdict


def isSafe(boggle, visited, i, j):
    return i >= 0 and i< len(boggle) and j >= 0 and j < len(boggle[0]) and not visited[i][j]

def searchWord(trie, boggle, i, j, visited, str):

    # if we found the word in trie dictionary
    # check if the trie (HashMap) contains the endSymbol *

    if '*' in trie:
        print(str)

    # check the 8 adjacent vertices
    rowIdx = [-1, -1, -1, 0, 0, 1, 1, 1]
    colIdx = [-1,  0,  1, -1, 1, -1, 0, 1]

    # mark it as visited
    visited[i][j] = True

    for k in range(8):
        # check in all 8 directions which character in the boggle is in the next Trie element
        if isSafe(boggle, visited, i+rowIdx[k], j+colIdx[k]) and boggle[i+rowIdx[k]][j+colIdx[k]] in trie:
            next_char = boggle[i+rowIdx[k]][j+colIdx[k]]
            searchWord(trie[next_char], boggle, i+rowIdx[k], j+colIdx[k], visited, str+next_char)

    visited[i][j] = False


def findWords(boggle, trie):

    # mark all characters as not visited
    visited = [[False for j in range(len(boggle[0]))] for i in range(len(boggle))]

    str = ""

    # traverse all Matrix elements
    for i in range(len(boggle)):
        for j in range(len(boggle[0])):

            # we start searching for word in dictionary
            # if we found a character which is child
            # of Trie root
            node = trie.root
            if boggle[i][j] in node:
                start_char = str + boggle[i][j]
                searchWord(node[start_char], boggle, i, j, visited, str+start_char)

if __name__ == "__main__":
    dictionary = ["GEEKS", "FOR", "QUIZ"]
    trie = SuffixTrie("GEEKS")

    # insert all dictionary words in Trie
    for i in range(1, len(dictionary)):
        trie.populateSuffixTreeFrom(dictionary[i])

    boggle = [['G','I','Z'],
              ['U','E','K'],
              ['Q','S','E']]

    findWords(boggle, trie)

    # res = trie.root
    # if trie['*']:
    #     print(res['G'])
    # chars = defaultdict(int)
    # chars = {'1': 1}
    # chars['2'] += 1
    # print(chars)

    val = {'k': {'*': 1}}
    if '*' in val['k']:
        print('Exists')
