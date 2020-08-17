"""
write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements
in the array if a sum cannot be generated the function should return '0'

- we need to identify a pattern

- identify the largest sum at a given location
- we will create copy of the given array and successively calculate the largest sum.
- check the larger element of 1st and 2nd element and store it in the 2nd place in the given array.
- traverse the array - starting from the 3rd location - and calculate which value is greater -
    the element before the current location (i-1)
                    OR
    the element 2 locations before the current element + the current element (i-2) + current_element_value

"""
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return maxSums[-1]

array = [75, 105, 120, 75, 90, 135]
# maxSubsetSumNoAdjacent(array)

"""
75+120+90
105+75+135
75+120+135
105+135

- what is the max sum at the given location in the array
"""
def subsets(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    print(maxSums)
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return maxSums[-1]

array = [105, 75, 120, 75, 90, 135]
print(subsets(array))


