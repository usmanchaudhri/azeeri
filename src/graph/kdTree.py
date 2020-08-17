import numpy as np
import pprint as pp

from sklearn.neighbors import KDTree

points = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
tree = KDTree(points, leaf_size=2, metric='euclidean')
nearest_dist, nearest_ind = tree.query(X=points[:1], k=3)         # k=2 nearest neighbours where
print(points[nearest_ind[0]])

"""
below is from sklearn documentation
"""
# rng = np.random.RandomState(0)
# X = rng.random_sample((10, 3))  # 10 points in 3 dimensions
# tree = KDTree(X, leaf_size=2)              # doctest: +SKIP
# dist, ind = tree.query(X[:1], k=3)                # doctest: +SKIP
# print(ind)  # indices of 3 closest neighbors
# print(dist)  # distances to 3 closest neighbors
