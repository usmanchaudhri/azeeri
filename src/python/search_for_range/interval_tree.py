"""
NOTE - complete it
"""
class IntervalTree:

    def __init__(self, low, high):
        self.interval = tuple(low, high)
        self.max = None
        self.left = None
        self.right = None

    def insert(self, low, high):
        currentNode = self

        while True:

            if currentNode is not None and currentNode.max < high:
                currentNode.max = high

            # if root's low value is smaller, then new interval goes to left subtree
            if low < currentNode.low:
                if currentNode.left is None:
                    currentNode.left = IntervalTree(low, high)
                    break
                else:
                    currentNode = currentNode.left

            else:   # new interval goes to the right subtree
                if currentNode.right is None:
                    currentNode.right = IntervalTree(low, high)
                    break
                else:
                    currentNode = currentNode.right




