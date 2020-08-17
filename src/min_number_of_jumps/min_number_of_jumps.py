"""
Min number of jumps to reach the end of the array
array -> [3,4,,2,1,2,3,7,1,1,1,3]
jumps -> [0,1,1,1,2,2,3,inf,inf,inf,4]
building smaller solutions to get bigger solution
"""
def min_number_of_jumps(array, n):
    # we will find out what is the minimum number of jumps needed to reach
    # any given point in the array starting from the beginning.
    # Starting from the beginning of the array we can either jump to the next
    # location or not, we would have to keep track of the minimum number of
    # jumps at the given index.

    # create array which will have the min number of jumps for that location
    jumps = [float("inf") for i in range(n+1)]
    print(jumps)

    jumps[0] = 0
    for i in range(1, len(array)):
        element = array[i]
        # current index is i
        # i can jump array[i]
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j]+1)
    jumps[-1]


if __name__ == "__main__":
    arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
    n = len(arr)
    min_number_of_jumps(arr, n)
