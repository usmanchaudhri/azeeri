
"""
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element
appears after the smaller number.
"""
def maxDiff(array):
    max_diff = array[1] - array[0]
    min_element = array[0]
    for i in range(1, len(array)):
        if array[i] - min_element > max_diff:
            max_diff = array[i] - min_element

        if array[i] < min_element:
            min_element = array[i]
    return max_diff

"""
Given an array arr[] of integers, find out the minimum difference between any two elements such that smaller element
appears after the larger number.

Solution -
- the idea here is to find the closest gap between two elements.
- we can sort the array to find the closest gap between two elements
- we can then take difference between two adjacent elements in the array, storing the smallest element at any given
    point.
- 
"""
# O nlog(n) | Space O(n)
def minDiff(array):
    prices = sorted(array)              # nlogn
    minElement = float("inf")
    for i in range(1, len(prices)):     # n
        if ( (prices[i] - prices[i-1]) < minElement and array.index(prices[i]) < array.index(prices[i-1])):
            minElement = prices[i] - prices[i-1]
    return minElement


if __name__ == "__main__":
    # array = [2, 3, 10, 1, 11, 6, 4, 8]
    # array = [5, 10, 3]
    # [20, 7, 8, 2, 5]
    array = [20, 7, 8, 2, 5]
    # print(minDiff(array))

    print(sorted(array, key=None, reverse=True ))
