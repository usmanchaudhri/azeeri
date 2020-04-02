"""
When to use Heap - We need heap when we want to keep track of the greatest or smallest value.
What is a Max Heap - The Max heap data structure ensures that the largest element is always at the top of the heap
and visa versa for Min Heap which ensures that the minimum element is always at the top.
This data structure helps in cases where we always need to maintain some sort of descending order among
elements, so, the largest or greater elements could be accessed as quickly.
- a Max heap is a complete binary tree.
- a Max heap is typically represented as an array.
- the root element will be at arr[0]

- current node -> i
- parent node  -> (i-1)//2
- left child   -> 2*i + 1
- right child  -> 2*i + 2

- a heap is not sorted
- root node is the smallest value in the heap
"""

class MinHeap:
    """
    We will use array to reflect our logical heap. Will do calculations to than
    """

    def __init__(self, array):
        self.heap = self.buildheap(array)

    def buildHeap(self, array):
        """
        - time O(n) | space O(1)
        - when starting to implement buildHeap() we will start with the parent of the last node in our heap which
        is going to be the last element of the heap array. We will calculate the parent of the last element using
        the formula: (len(array) -1 // 2)

        """
        firstParentIdx = (len(array)-1) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftUp(self, currentIdx, heap):
        """
        Sifting up is to move the current node up in the current tree.

        - calculate the parent of the current index
        - while current node element is less than the parent
        swap the current element with it's parent
        """
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def siftDown(self, currentIdx, endIdx, heap):
        """
        Sifting down is to move the current node down in the tree to find it's appropriate position

        When sifting down we have to compare the current node to it's two child nodes childOneIdx and childTwoIdx
        whichever is smaller we will compare it to the parent node. We will than swap the smaller of the two child
        nodes with the parent.

        - First we will calculate the value of one of the child nodes and check if that child node is not the among the leaf node.
        - Than we will check the second child node and check if that child is not the
        """
        childOneIdx = (currentIdx * 2) + 1
        while childOneIdx <= endIdx:        # check if our childOneIdx is not the leaf node if it is than there's no need to sift down
            childTwoIdx = (currentIdx * 2) + 2 if (currentIdx * 2) + 2 <= endIdx else -1    # if childTwo is not the leaf node
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childTwoIdx]: # if childTwo is less than childOne
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        """
        - swap the last and root value
        - pop off the last value since this is the value to be removed
        - sift down the value
        """
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        """
        append the value to the end of the heap and than sift up to than adjust the value accordingly
        """
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        """
        utility function which swaps the given index values
        """
        heap[i], heap[j] = heap[j], heap[i]

if __name__ == "__main__":
    lst = [2,5,6,10,3,15]
    firstParentIdx = (len(lst) - 1) // 2
    for currentIdx in reversed(range(firstParentIdx)):
        print(currentIdx)

    # print(reversed(lst))
    # print(list(reversed(lst)))
    # heapify(lst)
    # print(lst)
    # print(heappop(lst))
    # print((9 // 2))


