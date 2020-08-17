

def recursion(boggle, visited, i, j, str):
    visited[i][j] = True
    str = str + boggle[i][j]
    print(str)

    for k in range(2):
        recursion(boggle, visited, i+1, j+1, str)

    i = 0
    j = 1
    visited[i][j] = False


if __name__ == "__main__":
    boggle = [['G','I','Z'],
              ['U','E','K'],
              ['Q','S','E']]

    visited = [[False for j in range(len(boggle[0]))] for i in range(len(boggle))]
    str = ""
    i = 0
    j = 0
    recursion(boggle, visited, i, j, str)
    print(visited)

