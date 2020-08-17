# when comparing two ranges for overlap check when they don't overlap
def isOverlap(range1, range2):
    return (not range1[1] < range2[0]) and (not range1[0] > range2[1])

def isOverlapping(range1, range2):
    start = range1[0]
    end = range1[1]

    if range1[0] < range2[0]:
        if range2[0] <= range1[1]:
            end = max(range1[1], range2[1])
    elif range2[0] < range1[0]:
        if range1[1] <= range2[1]:
            start = range2[0]
            end = max(range1[1], range2[1])
        start = range2[0]

    print(start, end)

def overlappingIntervals(intervals):
    # sort the intervals by starting index
    intervals.sort(key=lambda x: x[0])

    mergedIntervals = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:      # overlapping intervals, adjust the 'end'
            end = max(interval[1], end)
        else: # non-overlapping interval, add the previous interval and reset
            mergedIntervals.append([start, end])
            start = interval[0]
            end = interval[1]

    # add the last interval
    mergedIntervals.append([start, end])
    return mergedIntervals

if __name__== "__main__":
    # print(isOverlap([17, 19], [23, 25]))
    # print(isOverlap([17, 24], [23, 25]))
    # print(isOverlap([17, 50], [23, 25]))
    # print(isOverlap([23, 25], [17, 50]))

    intervals = [[1, 5], [2, 3], [4, 6], [7, 8], [8, 10], [12, 15]]
    # res = overlappingIntervals(intervals)
    # print(res)
    isOverlapping([1, 5], [0, 3])