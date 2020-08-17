"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum
value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an
item, either pick the complete item or don’t pick it (0-1 property).
"""
def knapsack(W, weights, values, n):
    """
    :param W:       Total weight
    :param weights: list of available weight options
    :param values:  values against each weight option
    :param n:       counter
    :return:
    """
    if n == 0 or W == 0:
        return 0

    # if the current item is greater than the total weight don't add the item
    if weights[n-1] > W:
        return knapsack(W, weight, values, n-1)
    else:
        return max(knapsack(W, weights, values, n-1), values[n-1] + knapsack(W-weight[n-1], weights, values, n-1))

if __name__ == "__main__":
    # items = list(tuple())
    # items.append((1, 2))
    # items.append((3, 4))
    # for i in items:
    #     print(i[1])

    weight = [1, 4, 3, 7, 2, 6]
    value = [2, 2, 4, 1, 7, 8]
    optimalValue = knapsack(20, weight, value, len(weight))
    print(optimalValue)