"""
merge intervals
"""

def mergeIntervals(array):

    # sort based on the increasing order of the
    # start interval
    array.sort(key=lambda x: x[0])

    # array to hold the merged intervals
    m = []
    s = -10000
    max = -100000

    for i in range(len(array)):
        a = array[i]
        if a[0] > max:
            if i!=0:

            max = a[]


if __name__ == "__main__":
    array = [[6, 8], [1, 9], [2, 4], [4, 7]]
    mergeIntervals(array)
