"""
"""
# 20 - total weight which needs to be filled in the knapsack
# weights - available weights
# value - value against each weight
def knapsack(W, weights, values, n):
    if W == 0 or n == 0:
        return 0

    # check if the current weight is greater than the weight we are trying to make
    # than we are not skip the (n-1) item and move on to the next item
    if weights[n-1] > W:
        knapsack(W, weights, value, n-1)

    # we check how do we get the max value by adding the next weight or by not adding
    # the weight
    return max(knapsack(W, weights, values, n-1), values[n-1] + knapsack(W-weights[n-1], weights, values, n-1))


if __name__ == "__main__":
    weight = [1, 4, 3, 7, 2, 6]
    value = [2, 2, 4, 1, 7, 8]
    optimalValue = knapsack(20, weight, value, len(weight))
    print(optimalValue)


