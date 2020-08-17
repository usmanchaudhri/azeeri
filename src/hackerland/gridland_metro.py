"""

Solution:

- calculate how many total possible tracks are there in the matrix
-

"""

"""
number of rows = 4
number of columns = 4
total number of tracks = 16

tracks
"""
def findEmptyTrack(n, m, k, tracks):
    totalTracks = n*m
    coveredTracks = list(map(lambda x: abs(x[2] - x[1]) + 1, tracks))
    return (totalTracks - sum(coveredTracks))

def test_overlapping_track():
    n = 1
    m = 5
    k = 3
    tracks = [[1, 1, 2],
              [1, 2, 4],
              [1, 3, 5]]
    print(findEmptyTrack(n, m, k, tracks))

if __name__ == "__main__":
    # number of tracks
    # n = 4
    # m = 4
    # k = 3
    # tracks = [[2, 2, 3],
    #           [3, 1, 4],
    #           [4, 4, 4]]
    # emptyTracks = findEmptyTrack(n, m, k, tracks)
    # print(emptyTracks)
    test_overlapping_track()
