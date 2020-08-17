"""
Interval Search

- use left endpoint as the binary search key.
- apart from storing ranges also store the largest endpoint rooted at that node.
- we insert the node in the same way as binary tree insertion using the left key as the comparison node
    but afterwards on the way backup we update the max values at each node which might have to be updated due to
    this new node.

NOTE - complete it
"""
class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def intersect(self, new_interval):
        # when comparing two ranges
        curr_interval = self
        return (not curr_interval.high < new_interval.low) and (not curr_interval.low > new_interval.high)

class IntervalTree:
    def __init__(self, low, high):
        self.interval = Interval(low, high)
        self.max = float("-inf")
        self.left = None
        self.right = None

    def insert(self, low, high):
        currentNode = self
        while True:
            if currentNode is not None and currentNode.max < high:
                # set the max value at each node
                currentNode.max = high

            if low < currentNode.interval.low:
                # if root's low value is smaller, then new interval goes to left subtree
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

    def search(self, low, high):
        """ search for the [low, high] """
        curr_node = self
        while curr_node != None:
            if curr_node.interval.intersect(Interval(low, high)):
                return curr_node.interval
            elif curr_node.left == None:
                curr_node = curr_node.right
            elif curr_node.left.max < low:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

        return None

interval_tree = IntervalTree(1, 5)
interval_tree.insert(17, 19)
interval_tree.insert(5, 8)
interval_tree.insert(21, 24)
interval_tree.insert(15, 18)
# print(interval_tree)

interval = interval_tree.search(21, 24)
interval = interval_tree.search(1, 6)

print(f'[{interval.low}, {interval.high}]')

# print(tuple([1,2,3]))
# print(tuple('python'))
# py = tuple('python')
# print(py[0])
# print(py[1])
# print(py[2])
# print(tuple(1, 2))



