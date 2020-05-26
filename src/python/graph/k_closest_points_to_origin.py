"""
Given a list of points on the 2-D plane and an integer K. The task is to find K closest points to the origin and print them.
"""

# assuming that vertex is at point [0, 0]
def pCloset(points, k):
    points.sort(key=lambda k: k[0]**2 + k[1]**2)
    return points[:k]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(pCloset(points))

