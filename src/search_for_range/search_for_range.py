"""
We will use the binary search tree approach to first find the target number and than find the left extremity and
right extermity one after the other.

"""
def searchForRange(array, target):
    left = 0
    right = len(array) - 1
    finalRange = [-1, -1]

    alteredBinarySearch(array, target, 0, len(array) - 1, True, finalRange)   # run to find the left extremity
    alteredBinarySearch(array, target, 0, len(array) - 1, False, finalRange)   # run to find the right extremity

    return finalRange

# recursive solution
# time O(log(n)) | space O(log(n))
def alteredBinarySearch(array, target, left, right, goLeft, finalRange):
    """
    select a middle number in the array and start comparing it with the left and right index
    and traverse from there.
    """
    if left > right:    # if ever the left pointer crosses the right pointer
        return

    mid = (left + right) // 2
    if array[mid] < target:
        alteredBinarySearch(array, target, mid + 1, right, goLeft, finalRange)
    elif array[mid] > target:
        alteredBinarySearch(array, target, left, mid - 1, goLeft, finalRange)
    else:
        # found the target number now we need to check if there are more numbers to the left which
        # are equal to the target number
        if goLeft:
            # check the left bound index in array and check if the number immediate to the left of target number
            # is equal to the target number
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
            else:
                # run binary search again on the left array
                alteredBinarySearch(array, target, left, mid - 1, goLeft, finalRange)
        else:
            # check the right index bound and check if the immediate right
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                # run binary search again on the right array
                alteredBinarySearch(array, target, mid + 1, right, goLeft, finalRange)

# iterative solution
# time O(log(n)) | space O(1)
def alteredBinarySearch(array, target, left, right, goLeft, finalRange):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid  - 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    # found the left extremity
                    finalRange[0] = mid
                    return
                else:
                    # run binary search again to the left of array[mid]
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    # found the right extremity
                    finalRange[1] = mid
                    return
                else:
                    # run binary search to the right of array[mid]
                    left = mid + 1

if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    target = 45
    searchForRange(array, target)

