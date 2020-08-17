# brute force - list all combinations of size b than choose the one which has the desired sum
def makeCombination(n, k, b):
    # [1,2,3,4,5,6,7,8]
    array = [i+1 for i in range(8)]

    # for this array make combinations which are equal to the target sum
    # we first make sure the array is sorted.
    target = n
    size = b
    curr_sum = 0
    candidates = []
    combination(array, target, size, curr_sum, candidates, 0)

def combination(array, target, size, curr_sum, candidates, index):
    if curr_sum == target:
        # add the candidates combination here
        return

    if len(candidates) > size:
        return

    while index < len(array):
        curr_sum = curr_sum + array[index]
        candidates.append(array[index])
        index = index + 1
        combination(array, target, size, curr_sum, candidates, index)

        # remove the last number added to the candidate list since base case if met
        # add the candidates to the answer list
        candidates.remove(array[index])
        curr_sum = curr_sum - array[index]

    return candidates

if __name__ == "__main__":
    n = 12  # total sticks
    k = 8   # total boxes
    b = 3   # combination size
    makeCombination(12, 8, 3)


