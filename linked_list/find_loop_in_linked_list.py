"""
Detecting loop in a LinkedList
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        # node will be inserted at the head
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head

        # while slow_p and fast_p are not None keep traversing through the loop.
        while slow_p and fast_p and fast_p.next:
            # since fast is going twice the speed of slow, check whether fast_p.next is none or not
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# creating a loop for testing
llist.head.next.next.next.next = llist.head
if llist.detect_loop():
    print('Loop found')
else:
    print('No Loop found')








