
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        curr_node = self.root

        while True:
            if curr_node is None:
                curr_node = Node(value)
                break
            else:
                if curr_node.value < value:
                    if curr_node.right is None:
                        curr_node.right = Node(value)
                        break
                    else:
                        curr_node = curr_node.right

                else:
                    if curr_node.left is None:
                        curr_node.left = Node(value)
                        break
                    else:
                        curr_node = curr_node.left

    def height(self, tree):
        if tree is None:
            return 0
        else:
            lDepth = self.height(tree.left)
            rDepth = self.height(tree.right)

            if lDepth > rDepth:
                return 1+lDepth
            else:
                return 1+rDepth
