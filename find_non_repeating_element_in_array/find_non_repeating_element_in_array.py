
# time O(n) | space constant time
def find_single_element(nums):
    res = 0
    for num in nums:
        res ^=num
    return res

if __name__ == "__main__":
    array = [1, 1, 3, 5, 5, 6, 6]
    # print(find_single_element(array))

    x = 2
    y = 5
    # same as multiplying x by 2**y
    print(x<<4)


