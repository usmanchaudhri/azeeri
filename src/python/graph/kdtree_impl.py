
class Node(object):
    """
    a node in a kd-tree
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


