"""
Subset sum
"""
def subset_sum(nums, n, target):

    # define a bounding function where the condition will break the
    # recursion, otherwise, we will keep going
    if target == 0:
        return True
    if n == 0 and target != 0:
        # don't have enough weights remaining
        return False

    temp = subset_sum(nums, n-1, target)
    temp1 = subset_sum(nums, n-1, target - nums[n-1])

    return temp or temp1

array = [1, 2, 3, 4, 5, 6, 7, 8]
target = 12
n = len(array)

subset_sum(array, n, target)