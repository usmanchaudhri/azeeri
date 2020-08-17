"""

"""
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



""" For a linked list we always have reference to the head of the linked list 
    Merging the link list means we are change the reference of the pointers in 
    the existing linked lists to point to the new nodes.
"""
def mergeTwoLinkedList(headOne, headTwo):
    p1 = headOne
    p2 = headTwo
    previous = None
    if p1 == None:
        return p2

    if p2 == None:
        return p1

    # test1
    # headOne 1-3-5-7-9-None
    # headTwo 2-4-6-10-12-None

    # test2
    # headOne None
    # headTwo 2-4-6-10-12-None
    # we will traverse the two linked lists until we reach the end of either of the two linked list
    while p1 is not None and p2 is not None:
        if p1.value <= p2.value:
            previous = p1
            p1 = p1.next
        else:
            if previous is not None:
                previous.next = p2
            previous = p2
            p2 = p2.next
            previous.next = p1

    if p1 is None:
        previous = p2

    # we have merged the two lists and now have to return the starting list
    # which we can do by comparing the two lists and
    return headOne if headOne.value < headTwo.value else headTwo















