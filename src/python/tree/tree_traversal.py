class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)     # first recur the left child
        print(root.val)             # print the data on node
        printInorder(root.right)    # now recur on right child

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.left)
        print(root.val)

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)


root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("Inorder traversal of binary tree is")
printInorder(root)

print("Postorder traversal of binary tree is")
printPostorder(root)