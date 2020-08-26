"""
Return all indices which return pairs of numbers whose sum equal to target
"""

def find_pair_target_sum(numbers, target):
    numbers.sort()

    all_pairs = []
    startIdx = 0
    endIdx = len(numbers) - 1

    while startIdx < endIdx:
        sum = numbers[startIdx] + numbers[endIdx]
        if sum == target:
            all_pairs.append([numbers[startIdx], numbers[endIdx]])
        elif sum > target:
            endIdx -= 1
        elif sum <= target:
            startIdx +=1

    return all_pairs

numbers = [3, 9, 8, 4, 5, 7, 10]
res = find_pair_target_sum(numbers, 15)
print(res)