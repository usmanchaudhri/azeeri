"""
Search in sorted array of strings which may contain blanks
Given an array of strings. The array has both empty and non-empty strings. All non-empty strings are in sorted order.
Empty strings can be present anywhere between non-empty strings.
"""

# time O(n) | space (1)
# def search_in_sorted_array(array, target):
#     index = [i for i in range(len(array)) if array[i] == target]
#     return index[0]

# binary search
# time (log(n)) | space O(1)
def search_in_sorted_array(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if len(array[mid]) == 0:
            # linearly check non-empty strings on both left and right sides if we aland array[mid] as empty string
            goLeft, goRight = mid - 1, mid + 1
            while True:
                if goLeft < left and goRight > right:
                    return -1
                if goRight <= right and len(array[goRight]) != 0:
                    mid = goRight
                    break
                if goLeft >= left and len(array[goLeft]) != 0:
                    mid = goLeft
                    break

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid

if __name__ == "__main__":
    array = ["for", "", "", "", "geeks", "ide", "", "practice", "", "", "quiz", "", ""]
    print(search_in_sorted_array(array, "quiz"))