"""
Question -

Design a class to find the kth largest element in a stream. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add, return
the element representing the kth largest element in the stream.
"""
from heapq import heapify, heappush, heappop, heappushpop

class KthLargest:
    """
    We will use the heap data structure here since by it's nature heap maintains either the ascending or descending order
    and we only maintain k elements in our heap. This way when we would need the kth largest element we can just send the top
    most element in the heap without doing any further processing.
    """
    def __init__(self, k, nums):
        self.k = k
        self.k_heap = nums
        heapify(self.k_heap)
        while len(self.k_heap) > k:
            heappop(self.k_heap)

    def add(self, val):
        if len(self.k_heap) < self.k:
            heappush(self.k_heap, val)
        else:
            heappushpop(self.k_heap, val)
        return self.k_heap[0]

if __name__ == "__main__":
    nums = [2,5,6,10,3,15]
    print(KthLargest(6, nums).add(7))


    

