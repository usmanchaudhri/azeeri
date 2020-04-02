"""
Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

Input: {1, 2, 3, 7}, S=6
{1, 2, 3} = 6

Using Dynamic programming we have to see if we can find all sums upto the total sum using the numbers in the num array.

- For sum 6 we will find out if we can get to the sum for the following numbers [1,2,3,4,5,6] which will successively lead to 6
- We have a list of numbers {1, 2, 3, 7} so we will see if for a given sum whether we will include or exclude the number at the given index in num[].
    * Exclude the number. In this case, we will see if we can get the sum 's' from the subset excluding this number => dp[index-1][s]
    * Include the number if its value is not more than 's'. In this case, we will see if we can find a subset to get the remaining sum =>
    dp[index - 1][s - num[index]]
"""

def can_partition(num, sum):
    """
            sum [0][1][2][3][4][5][6]
        num
        {1}
      {1,2}
    {1,2,3}
  {1,2,3,7}
    - we have to make all sum given along x-axis with the set of numbers given along y-axis.
    - for each point (x, y) we have to choose whether we can make the sum (which is along x-axis)
    with the number or without the number - given along y-axis.
    1) initialize two dimensional array with sum across x-axis and the given numbers along y-axis.
    2) populate the sum=0 column as we can always form '0' with an empty set hence that sum=0 column will all be True
    3) populate the first row where for each sum it will be formed if the number == sum
    4) we have now populated the first column and first row of the two-dimensional matrix
    5) now we will process all the remaining subsets with the following logic:
        - for each i in numbers:
            for each sum in sums:
                if we can get the 'sum' without the number at index i -> 2Darray[i-1][sum] == true:
                    than assign (2Darray[num][sum] = 2Darray[num-1][sum])
                else if sum is greater than or equal to number at index i than incude the number and see if
                    we can find a subset to get the remaining sum.
                    2Darray[num][sum] = 2Darray[i-1][sum-num[i]]

            return the last element of the two-dimensional array which is the bottom-right corner of the 2Darray[n-1][sum]
    """

    n = len(num)
    dp = [[False for x in range(sum+1)] for y in range(n)]

    # populate the sum = 0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # for each sum it will be formed if the num == sum
    for s in range(1, sum+1):
        # dp[0][s] = True if num[0] == s else False
        dp[0][s] = num[0] == s

    # Now process for all the subsets
    for i in range(n):
        for s in range(sum+1):
            if dp[i-1][s]:
                # if we can get the sum 's' without the number at index 'i'
                dp[i][s] = dp[i-1][s]
            elif s >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][s] = dp[i-1][s - num[i]]

    # the bottom-right corner will have own answer
    return dp[n-1][sum]


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
