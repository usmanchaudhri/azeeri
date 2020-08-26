# tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        currentNode = self.root
        while True:
            if currentNode is None:
                currentNode = Node(value)
                break
            else:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = Node(value)
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = Node(value)
                        break
                    else:
                        currentNode = currentNode.right

    def contains(self, value):
        current_node = self.root
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True

        return False

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)

