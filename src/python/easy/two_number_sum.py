"""
Given an array of integers, return the indices of the two numbers whose sum is equal to a given target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

- we will first sort the input array so the array is in ascending order
- we will than use the ascending order property to find the two number sum.
- we now know that the array is in ascending order, so, we will set two pointers
    at the beginning(left) and the end(right) of the array.
- we will add the (array[left] + array[right]) and see if the sum is greater than the target sum
    which would mean that the array[right] number has to be smaller in-order to make the target sum.
    And so we would decrement the right pointer and than recalculate the (array[left] + array[right])
    If (array[left] + array[right]) less than target sum we will increment the left pointer.

Sample input array: [3,5,-4,8,11,1,-1,6]
Target sum: 10
Sample Output: [-1, 11]
"""
def two_sum(array, targetSum):
    sumCombinations = [[]]
    array.sort()
    right = len(array) -1
    for left in range(len(array) -1):
        potentialSum = array[left] + array[right]
        if potentialSum == targetSum:
            sumCombinations.append([array[left], array[right]])
        elif potentialSum > targetSum:
            right -= 1

    return sumCombinations

if __name__ == "__main__":
    two_sum([3,5,-4,8,11,1,-1,6], 10)