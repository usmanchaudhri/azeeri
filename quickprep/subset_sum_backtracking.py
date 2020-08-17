"""
subset sum using backtracking
"""

# O(2^n)
def subset_sum_backtracking(numbers, pos, target_sum, tmpSum, size, found):
    if target_sum == tmpSum:
        # found = True
        # print(found)
        return True

    # generate nodes along the breadth
    for i in range(pos, size):
        if tmpSum + numbers[i] <= target_sum:
            tmpSum += numbers[i]

            res = subset_sum_backtracking(numbers, i+1, target_sum, tmpSum, size, found)
            if res:
                break
            tmpSum -= numbers[i]

    return True

numbers = [1, 3, 5, 2]
print(subset_sum_backtracking(numbers, 0, 6, 0, len(numbers), False))