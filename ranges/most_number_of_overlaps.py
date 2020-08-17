"""
Given a list of ranges such as : [(6, 10), (-2, 4), (3, 5)], find the range with the highest number of overlaps.
In this example, that would be (3, 4) which has 2 ranges overlapping.

         (6               10)
(-2   4)
    (3  5)
"""
def find_max_overlapping(ranges):
    start = []
    end = []
    for range in ranges:
        start.append(range[0])
        end.append(range[1])

    start.sort()
    end.sort()

    curr_overlap_counter = 0
    max_overlap_counter = 0

    s = len(start)
    e = len(end)
    i = 0
    j = 0
    while i < s and j < e:
        if start[i] < end[j]:
            curr_overlap_counter += 1
            max_overlap_counter = max(max_overlap_counter, curr_overlap_counter)
            i += 1
        else:
            # when we identify that this start is not less than the end point that means
            # the range is not overlapping but we are one step ahead and we need to reduce the counter over lap
            # count.
            curr_overlap_counter -= 1
            j += 1

    return max_overlap_counter

ranges = [(6, 10), (-2, 4), (3, 5)]
# max_overlap_count = find_max_overlapping(ranges)
# print(max_overlap_count)

ranges.sort(key=lambda x: x[0])
print(ranges)





