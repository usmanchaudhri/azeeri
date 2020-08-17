
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        curr = self
        p1 = None
        p2 = curr.head
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

