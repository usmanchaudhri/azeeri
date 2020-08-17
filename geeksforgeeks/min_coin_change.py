"""
The algorithm uses a greedy approach - inorder to calculate min number of denominations for a target value,
we will calculate the minimum denomination used for target (value-n), (value-3), (value-2), (value-1)
and as a result we will end up calculating the minimum denominations for the target value.

Denominations are represented row wise and the amount is presented column wise
        1   2   3   4   5   6   7   8   9  10
    5   0   0   0   0   1
    10
    25

              1    2    3    4    5    6    7    8    9    10
numOfCoins= [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

- we will find the minimum number of coins for every amount leading to the target amount 10
- once the complete numOfCoins array is filled the last index will be the minimum number of coins
needed to make the target amount.
"""
# m*n => (n^2)
# O(n^2) time | space O(n)
def min_coin_change(amount, denoms):
    numOfCoins = [float("inf") for amt in range(amount+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])

    # return the last value in numOfCoin if "inf" is not present, otherwise, return -1
    return numOfCoins[amount] if numOfCoins[amount] != float("inf") else -1

if __name__ == "__main__":
    coins = [25, 10, 5]
    v = 10
