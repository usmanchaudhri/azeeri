"""
Partitioning by Elements in the entire set.

Let's divide the task of selecting "r" elements from "n" items by inspecting the items one by one. For each item in the
set, we can either include it in the selection or exclude it.

If we include the first item, then we need to choose "r-1" elements from the remaining "n-1" items. On the other hand
, if we discard the first item, then we need to select "r" elements out of the remaining "n-1" items.

This can be expressed as:
C(n, r) = C(n-1, r-1) + C(n-1, r)

"""
def helper(combinations, data, start, end, index):
    if index == len(data):
        d = data[:]
        combinations.append(d)
    elif start <= end:
        data[index] = start
        helper(combinations, data, start+1, end, index+1)
        helper(combinations, data, start+1, end, index)

def generate(n, r):
    combinations = []
    helper(combinations, [None] * r, 0, n-1, 0)
    return combinations

def generate_iterative(n, r):
    combinations = []
    combination = []

    # initialize with lowest lexicographic combination which in this case are 0 and 1
    for i in range(0, r):
        combination.append(i)
    while combination[r-1] < n:
        combinations.append(combination[:])

        # generate next combination in lexicographic order
        # run t for 1 and 0 (1 -> 0)
        t = r - 1
        while t != 0 and combination[t] == n - r + t:
            t -= 1

        combination[t] += 1
        for i in range(t+1, r):
            combination[i] = combination[i-1] + 1

def test(data):
    d = data[:]     # copy of data, modifying d will not change data
    d = data        # d is reference of data, modifying d will change data as well
    d[0] = 'aaaa'

if __name__ == "__main__":
    # choose 2 elements from a set of 10 elements
    r = 2
    n = 5
    # combinations = generate(n, r)
    # print(combinations)
    generate_iterative(n, r)

    # data = ['z', 'x', 'c']
    # test(data)
    # print(data)