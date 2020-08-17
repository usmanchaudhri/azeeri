"""
subset sum using combinations
"""

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    if s == target:
        print("sum(%s)=%s" % (partial, target))

    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

numbers = [3, 9, 8, 4, 5, 7, 10]
subset_sum(numbers, 15)