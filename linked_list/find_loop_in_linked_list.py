"""
Detecting loop in a LinkedList and remove the loop
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

                # uncomment if we want to remove loop from the linked list
                self.remove_loop(slow_p)
                return 1
        return 0

    def remove_loop(self, loop_node):
        """
        - start with two pointers ptr1 and ptr2 which will point to head and the loop_node
        - ptr2 will start from loop_node and it will traverse the linked list
        - ptr2 will traverse the linked list until ptr2.next != loop_node and ptr2.next != ptr1
        - if ptr2.next == ptr1 which is the head
        """
        # start two pointers ptr1 which points to head and ptr2 which points to the loop node
        ptr1 = self.head
        while True:
            # this is the loop node
            ptr2 = loop_node

            # traverse ptr2 node until one of the two conditions are met -
            #   ptr2 reaches the loop_node
            #   ptr2 reaches the ptr1 node which is the head
            while ptr2.next != loop_node and ptr2.next != ptr1:
                ptr2 = ptr2.next

            if ptr2.next == ptr1:
                # ptr2 points to the head, we can break the loop and point the
                # ptr2.next to None
                break
            ptr1 = ptr1.next

        ptr2.next = None

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








