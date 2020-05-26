"""
A graph can be represented as a Matrix
"""

# queue node used in BFS
class Node:

    def __init__(self, x, y, node):
        # x,y represents coordinates of a cell in matrix
        self.x = x
        self.y = y
        self.parentNode = node  # maintain parent node for printing the final path

    def __str__(self):
        return "(" + self.x + "," + self.y + ")"

class ShortestPathFinder:

    """
    find the shortest route in the matrix from source (x,y) to
    destination cell (N-1, N-1) - the last cell.
    """
    def findPath(self, matrix, x, y):
        N = len(matrix)

        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        # all possible directions we can move
        row = [-1, 0, 0, 1]     # only move one cell to the left or right
        col = [0, -1, 1, 0]     # only move one cell up or down

        queue = [Node(x, y, None)]      #
        visited = set()

        while len(queue) > 0:       # while queue is not empty keep going
            current = queue.pop(0)
            if current.x == rows and current.y == cols:
                return current

            # value of current cell
            current_value = matrix[current.x][current.y]
            for i in range(4):
                # check all four possible coordinates using value of current cell

                # get next position coordinates using value of current cell
                x = current.x + row[i] * current_value
                y = current.y + col[i] * current_value

                # check if it possible to go to the next position
                if(isValid(x, y, N)):

                    # construct next cell node
                    new_node = Node(x, y, current)

                    key = (new_node.x, new_node.y)

                    if key not in visited:
                        # push it into the queue and mark it as visited
                        queue.append(new_node)
                        visited.add(key)

        # return None is path is not possible
        return None


def isValid(x, y, sizeOfMatrix):
    # the function return false if point (x,y) is not a valid position
    return (x >= 0 and x < sizeOfMatrix) and (y >= 0 and y < sizeOfMatrix)


if __name__ == "__main__":
    matrix = [
        [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
        [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
        [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
        [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
        [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
        [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
        [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
        [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
        [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
        [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    ]

    res = ShortestPathFinder().findPath(matrix, 0, 0)
    print(res)
    # queue = []
    # queue.append(1)
    # queue.append(2)
    # queue.append(3)
    # queue.append(4)
    # print(queue.pop())
