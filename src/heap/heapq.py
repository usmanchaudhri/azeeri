from heapq import heapify, heappop, heappush

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 11)
heappush(heap, 12)
heappush(heap, 9)
heappush(heap, 20)

# print min element in heap
print(heap)
print(heap[0])

# print the elements of heap
print('\n Elements of heap')
for i in heap:
    print(i)

element = heappop(heap)
print('Pop element of heap ', element)
# print(heap[0])

print('Max element of heap', heap[-1])
print('Max element of heap', heap[-2])
print('Max element of heap', heap[-3])

import heapq
heap = [(1, 'one'), (10, 'ten'), (5, 'five')]
heapq.heapify(heap)
for x in heap:
    print(x)

