
class Node:
    def __init__(self, data):
        self.item = data
        self.nextRef = None
        self.previousRef = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print('list is not empty')

    def insert_at_start(self, data):
        if self.start_node == None:
            new_node = Node(data)
            self.start_node = new_node
            print('node inserted')
            return
        new_node = Node(data)
        new_node.nextRef = self.start_node
        self.start_node.previousRef = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node == None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node

        # traverse the linked list to the end
        while n.nextRef is not None:
            n = n.nextRef

        new_node = Node(data)
        n.nextRef = new_node
        new_node.previousRef = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print('list if empty')
            return
        else:
            n = self.start_node

            # first find the item in the list
            while n is not None:
                if n.item == x:
                    break
                n = n.nextRef

            if n is None:
                print('item not in the list')
            else:
                new_node = Node(data)
                new_node.previousRef = n
                new_node.nextRef = n.nextRef
                # this could be None if adding item after tail
                if n.nextRef is not None:
                    n.nextRef.previousRef = new_node
                n.nextRef = new_node

    def insert_before_item(self, x, data):
        if self.start_node == None:
            print('list is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nextRef
            if n is None:
                print('item does not exit in list')
            else:
                new_node = Node(data)
                new_node.nextRef = n
                new_node.previousRef = n.previousRef
                # this could be None in case if adding item before head
                if n.previousRef is not None:
                    n.previousRef.nextRef = new_node
                n.previousRef = new_node

    def traverse_list(self):
        if self.start_node is None:
            print('list if empty')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nextRef

    def delete_at_start(self):
        if self.start_node is None:
            return
        if self.start_node.nextRef is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nextRef
        self.start_node.previousRef = None

    def delete_at_end(self):
        if self.start_node is None:
            return
        if self.start_node.nextRef is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nextRef is not None:
            n = n.nextRef
        n.previousRef.nextRef = None

    # x is the value to delete in the linked list
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print('list if empty')
            return
        if self.start_node.nextRef is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print('item not found')

        if self.start_node.item == x:
            self.start_node = self.start_node.nextRef
            self.start_node.previousRef = None

        n = self.start_node

        # find the desired node
        while n is not None:
            if n.item == x:
                break
            n = n.nextRef

        if n.nextRef is not None:
            n.previousRef.nextRef = n.nextRef
            n.nextRef.previousRef = n.previousRef
        else:
            # if last node is to be deleted
            if n.item == x:
                n.previousRef.nextRef = None

    def reverse_linked_list(self):
        if self.start_node is None:
            print('list is empty')
            return

        # start with reversing the first two nodes only
        p = self.start_node
        q = p.nextRef
        p.nextRef = None
        p.previousRef = q

        while q is not None:
            q.previousRef = q.nextRef
            q.nextRef = p
            p = q
            q = q.previousRef
        self.start_node = p

    # what is following is going to become next, what is next is going to be previous
    # we will track three pointers p1, p2, p3
    # p1 will follow p2 which will follow p3 and at the end p1 will become the start_node

    # breakdown
    # - initialize p1 and p2 to none and start_node
    # - initialize p3 to point to the element next to p2 (p2.nextRef)
    # - set the previous and next references for p2 and since we are inverting the linked list
    #       * p2's next reference will now be p1
    #       * p2's previous reference will now be p3
    # - once we set values for p2 we will now move further down in the linked list
    #       * move p1 to p2
    #       * move p2 to p3
    # - in the end p1 will become the start_node
    def reverse(self):
        p1, p2 = None, self.start_node
        while p2 is not None:
            p3 = p2.nextRef
            p2.nextRef = p1
            p2.previousRef = p3

            p1 = p2
            p2 = p3
        self.start_node = p1

if __name__ == "__main__":
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_in_empty_list(50)

    new_linked_list.insert_at_start(10)
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_start(18)

    new_linked_list.insert_at_end(29)
    new_linked_list.insert_at_end(39)
    new_linked_list.insert_at_end(49)

    new_linked_list.insert_after_item(50, 65)

    new_linked_list.insert_after_item(29, 100)

    new_linked_list.traverse_list()

    print('Reverse linked list: ')
    # new_linked_list.reverse_linked_list()
    new_linked_list.reverse()

    new_linked_list.traverse_list()
























