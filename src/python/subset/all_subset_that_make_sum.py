
def total_subsets_matching_sum(numbers, target):
    array = [1] + [0] * target
    for current_numbers in numbers:
        for num in range(target - current_numbers, -1, -1):
            if array[num]:
                array[num + current_numbers] += array[num]
    return array[target]


if __name__ == "__main__":
    # print('')
    numbers = [1, 3, 2, 5, 4, 9]
    print(total_subsets_matching_sum(numbers, 9))

    # array = [1] + [0]
    # print(array)