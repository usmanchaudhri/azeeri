"""
deque()
heapify, heappush, and heappop
plan list

- check how deque works for tuples
"""

# using deque
from collections import deque

# simple queue operation
que = deque()
que.append(11)
que.append(3)
que.append(9)
# print(que)
# print(que.popleft())
# print(min(que))
# print(max(que))
# que = sorted(que)
# print(que)
# print(que.pop())

# queue operation for a tuple
que = deque()
que.append(('c', 11))
que.append(('z', 3))
que.append(('b', 9))
print(que)

def sort_que(element):
    return element[1]

print(min(que))                           # uses the first element to sort the queue
# print(min(que, key=lambda x: x[1]))     # uses the explicitly specified second element to sort the queue
print(min(que, key=sort_que))

# using PriorityQueue()
from queue import PriorityQueue

print('*** PriorityQueue ***')
que = PriorityQueue()
que.put(11)
que.put(3)
que.put(9)
print(que.queue)

que = PriorityQueue()
que.put((11, 'c'))
que.put((3, 'a'))
que.put((9, 'b'))
print(que.queue)

from heapq import heappop, heappush
import heapq

heap = [(1, 'one'), (10, 'ten'), (5, 'five')]
heapq.heapify(heap)
for x in heap:
    print(x)

print('Heapify')
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))


