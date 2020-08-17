"""
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form
an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the
Depth-first-search approach (specifically navigating the tree from left to right), stores all of the nodes' names
in the input array, and returns it.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

    # def __str__(self):
    #     print(self.name)
    #     for i in range(len(self.children)):
    #         print(self.children[i].name)

if __name__ == "__main__":
    node = Node("A")
    node.addChild("B")
    node.addChild("C")
    node.addChild("D")
    print(node)
