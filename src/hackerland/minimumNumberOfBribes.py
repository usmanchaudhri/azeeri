"""
"""
# def minimumNumberOfBribes(persons):
#     for i in range(len(persons)-1, -1):
#         j = 0
#
#         bribes = persons[i] - (i+1)
#         if bribes > 2:
#             print('Too Chaotic')
#             return
#
#         if persons[i]-2 > 0:
#             j = persons[i] - 2
#

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):

        # subtracts the value[i] with the index position to determine
        # how many position this number of off in the queue.
        # if the element at position i is off by more than 2 elements
        # we will not proceed any further and exist the program
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return

        # calculate j which is going to be the starting index of
        # and i will be the current index which will be the end.
        # than we traverse from j to i to determine how many places
        # the elements have moved inorder to determine how many
        # bribes were given in that range. The criteria for bribes
        # is that if q[i] > q[i]
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    return bribes

if __name__ == "__main__":
    test_case1 = [2, 1, 5, 3, 4]
    test_case2 = [2, 5, 1, 3, 4]
    test_case3 = [1, 2, 5, 3, 4, 7, 8, 6]

    print(minimumBribes(test_case1))
    # print(minimumBribes(test_case2))
    # print(minimumBribes(test_case3))
    # print(minimumBribes(test_case3))



