"""

"""
def isSubsetSum(set, n, target):

    # base case
    if target == 0:
        return True
    if n == 0 and target != 0:
        return False

    # check if sum can be obtained by any of the following
    # a) including the last element
    # b) excluding the last element
    return isSubsetSum(set, n-1, target) or isSubsetSum(set, n-1, target-set[n-1])

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 12
    n = len(array)
    print(isSubsetSum(array, n, target))


