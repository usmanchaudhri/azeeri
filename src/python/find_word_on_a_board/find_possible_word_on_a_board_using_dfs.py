"""
Boggle (Find all possible words in a board of characters) | Set 1
Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to any of 8
adjacent characters, but a word should not have multiple instances of same cell.
"""
# from recurse
# import trace
# from pudb import set_trace
# set_trace()

def isWord(word):
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    if word in dictionary:
        return True
    return False

def isSafe(boggle, visited, i, j):
    return i >= 0 and i< len(boggle) and j >= 0 and j < len(boggle[0]) and not visited[i][j]

def findWordsUtil(boggle, visited, i, j, str):
    # a recursive function to print all words present on boggle

    # mark current cell as visited and append current character
    # to str
    visited[i][j] = True
    str = str + boggle[i][j]

    # if str is present in dictionary, then print it
    if (isWord(str)):
        print(str)

    # check the 8 adjacent vertices
    rowIdx = [-1, -1, -1, 0, 0, 1, 1, 1]
    colIdx = [-1,  0,  1, -1, 1, -1, 0, 1]

    # traverse 8 adjacent cells of boggle[i][j]
    # recur for all connected neighbour
    for k in range(8):
        # loop to
        if isSafe(boggle, visited, i+rowIdx[k], j+colIdx[k]):
            findWordsUtil(boggle, visited, i+rowIdx[k], j+colIdx[k], str)

    # erase current character from String and mark visited of current cell as False
    # str = del str[len(str) - 1]

    # once we check all possible 8 directions for the current character at boggle[i][j]
    # we will mark the current character in visited[i][j] as False since now we will back
    # track to the previous character and now the for loop will run for all other possible
    # direction than the current character was on since the loop already has executed for
    # the current character [i+rowIdx[k]][j+colIdx[k]]
    visited[i][j] = False
    # str = str[:len(str) - 1]

def findWords(boggle):

    # mark all characters as not visited
    visited = [[False for j in range(len(boggle[0]))] for i in range(len(boggle))]

    str = ""

    # consider every character and look for all words
    # starting with this character
    for i in range(len(boggle)):
        for j in range(len(boggle[0])):
            findWordsUtil(boggle, visited, i, j, str)

def main():
    boggle = [['G','I','Z'],
              ['U','E','K'],
              ['Q','S','E']]
    findWords(boggle)

if __name__ == "__main__":
    boggle = [['G','I','Z'],
                ['U','E','K'],
                ['Q','S','E']]
    findWords(boggle)
    # isWord(boggle, "GEEKS")
    # str = "GEEKS"
    # print(str.replace())
    # print(len(str))
    # print(len(str)-1)
    # print(str[:1])
    # print(str[:len(str)-1])