"""
merge overlapping ranges
"""
def merge_overlapping_ranges(ranges):
    # sort the ranges with start
    ranges.sort(key=lambda x: x[0])
    print(ranges)

    start = ranges[0][0]
    end = ranges[0][1]

    final_ranges = []
    for i in range(1, len(ranges)):
        curr_interval = ranges[i]
        if curr_interval[0] <= end:
            # overlapping ranges found, adjust the end
            end = max(curr_interval[1], end)
        else:
            final_ranges.append([start, end])

            # reset the range for the next comparison
            start = curr_interval[0]
            end = curr_interval[1]

    final_ranges.append([start, end])
    return final_ranges

intervals = [[1, 5], [2, 3], [4, 6], [7, 8], [8, 10], [12, 15]]
ranges = merge_overlapping_ranges(intervals)
print(ranges)