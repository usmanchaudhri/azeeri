"""
USING DYNAMIC PROGRAMMING TO CALCULATE THE TARGET SUM USING GIVEN ELEMENTS IN AN ARRAY.

- We are using dynamic programming to see if we can make target (n-1), (n-2), (n-3)...and so on using the elements given
    in the array.
- Suppose we have to make target 9 with given elements in the array [1, 2, 3, 4, 5, 6, 7, 8].
- We will create a two-dimensional table where the target will be along column and the given set of array
    will be along rows.
- So 'i' is the set and 'j' is target.
- if j < i which means that if the target is less than the number than copy the value of the previous array element
    which was used to make the same target J.
- if j >= i than subtract j from the value at 'i' in set and see what value we have in our DP table for
    dp[i-1][j - array[i-1]]. So,
    set[i][j] = dp[i-1][j] OR dp[i-1][j-set[i-11]] whichever is true.


    0   1   2   3   4   5   6   7   8   9
0   t   f   f   f   f   f   f   f   f   f
1   t
2   t
3   t
4   t
5   t
6   t
7   t
8   t


- Reconstructing numbers from table:
    0   1   2   3   4   5   6   7   8   9  10  11  12
0   1   0   0   0   0   0   0   0   0   0   0   0   0
1   1   1   0   0   0   0   0   0   0   0   0   0   0
2   1   1   1   1   0   0   0   0   0   0   0   0   0
3   1   1   1   1   1   1   1   0   0   0   0   0   0
4   1   1   1   1   1   1   1   1   1   1   1   0   0
5   1   1   1   1   1   1   1   1   1   1   1   1   1
6   1   1   1   1   1   1   1   1   1   1   1   1   1
7   1   1   1   1   1   1   1   1   1   1   1   1   1
8   1   1   1   1   1   1   1   1   1   1   1   1   1

"""
# for printing all subsets for a given sum
# print_subsets_rec(subset, array, n-1, 12, []);
def print_subsets_rec(dp, array, row, target, p):

    # if we reached end and sum is non-zero. We print p[]
    # only if arr[0] is equal to sum or dp[0][sum] is true
    if row == 0 and target != 0 and dp[0][target]:
        p.append(array[row])
        print(p)
        p.clear()
        return

    # if sum becomes 0
    if row == 0 and target == 0:
        print(p)
        p.clear()
        return

    # if given sum can be achieved after ignoring
    # the current element
    if dp[row-1][target]:
        # create a new array to store path
        b = [p]
        print_subsets_rec(dp, array, row-1, target, b)

    if target >= array[row] and dp[row-1][target - array[row]]:
        p.append(array[row])
        print_subsets_rec(dp, array, row-1, target-array[row], p)


# O(n^2)
def isSubsetSum(set, n, target):

    # sum from 0 to target are columns. And the given set of numbers
    # array are along rows
    subset = [[False for i in range(target+1)] for i in range(n+1)]

    # if sum is 0, than answer is true
    # 0 can be made by any number
    # setting the first column
    for i in range(n + 1):
        subset[i][0] = True

    # if sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, target+1):
        subset[0][i] = False

    # Fill the subset table in bottom up manner
    for i in range(1, n+1):
        for j in range(target+1):       # j is the sum all the way to the final sum - target.
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = subset[i-1][j] or subset[i-1][j-set[i-1]]

    # uncomment this code to print table
    # for i in range(n + 1):
    #     for j in range(target + 1):
    #         print(subset[i][j], end=" ")
    #         print()

    print_dp_table(subset)
    print_subsets_rec(subset, array, n-1, 12, []);

    # return subset[n][target]
    # return subset

def print_dp_table(dp_table):
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in dp_table]))
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in dp_table]))


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 12
    n = len(array)
    print(isSubsetSum(array, n, target))

    array = [1, 1, 1]
    target = 12
    n = len(array)
    print(isSubsetSum(array, n, target))




