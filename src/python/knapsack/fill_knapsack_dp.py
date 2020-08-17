"""
"""
# 20 - total weight which needs to be filled in the knapsack
# weights - available weights
# value - value against each weight
# 1-W along column and given weights along rows
def knapsack(W, weights, values, n):
    dp = [[0 for j in range(W)] for i in range(n)]
    print(dp)

    #   0 1 2 3 4
    # 0 0 0 0 0 0
    # 1 0
    # 2 0
    # 3 0
    # 4 0

    # fill first column with '0'
    for i in range(n+1):
        dp[i][0] = 0

    # fill first row with '0'
    for i in range(W+1):
        dp[0][i] = 0

    for i in range(n+1):        # the list of given weights
        for w in range(W+1):
            if weights[i] <= W:
                # what we are storing is the value which is used to make w weight
                dp[i][w] = max(values[i] + dp[i][W - weights[i]], dp[i][w])
            else:
                # since we didn't included the last weight
                # copy the previous weight from the list of given weights which was used to make 'w'
                dp[i][w] = dp[i-1][w]

    # the last element is the max
    dp[n][W]

if __name__ == "__main__":
    weight = [1, 4, 3, 7, 2, 6]
    value = [2, 2, 4, 1, 7, 8]
    optimalValue = knapsack(20, weight, value, len(weight))
    print(optimalValue)


