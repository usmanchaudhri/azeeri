class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        # inserting element at the head of the link list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_1(self, value):
        curr = self
        # inserting element at the head of the link list
        new_node = Node(value)
        new_node.next = curr.head
        curr.head = new_node

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def reverse(self):
        curr = self
        p1 = None
        p2 = curr.head

        # traverse till the end of the link list
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

llist = LinkedList()
llist.insert_1(10)
llist.insert_1(11)
# llist.insert(10)
# llist.insert(11)
# llist.insert(12)
print("PRINTING LINK LIST")
llist.print()

