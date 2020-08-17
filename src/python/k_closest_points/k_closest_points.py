"""

"""
from math import sqrt
from queue import PriorityQueue
from heapq import heappush

# Time - to find the distance from every point is O(n) and to sort the array is O(n log n)
# Space = O(1)
def k_closest_points(points, k):
    points.sort(key=lambda k: sqrt(k[0]**2 + k[1]**2))
    return points[:k]

points = [[-2, 2], [1, 3]]
# print(k_closest_points(points, 2))

q = PriorityQueue()
q.put([1,2])
q.put([10, 100])
q.put([8, 1])
q.put([4, 100])
q.put([44, 100])



while not q.empty():
    print(q.get())



