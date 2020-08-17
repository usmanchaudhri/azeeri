
# we will find out what are the minimum weights needed to get all weights from 0 to W
def knapsack(W, weights, value, n):
    # build a table where the total weights from 1 to W will be listed column wise
    # and the weights given will be row wise.
    k = [[0 for j in range(W+1)] for i in range(n+1)]

    # fill the first column with all zero's because for the first column
    # we are trying to make weight w zero, so, we don't need any weights.
    for i in range(n+1):
        k[i][0] = 0

    # fill the first row with all zero's because with 0 as weight we cannot make any weight W.
    for i in range(W):
        k[0][i] = 0

    for i in range(n+1):           # the list of weights given
        for w in range(W+1):       # 0 to total weight W
            if weights[i-1] <= w:
                # either add the new weight to the knapsack or not, if not, then just keep the previous value
                # at location i-1 for weight w
                k[i][w] = max(value[i-1] + k[i-1][W - weights[i-1]], k[i-1][w])
            else:
                # just copy the last weight which was used to make weight w.
                k[i][w] = k[i-1][w]

    # the last element will have the maximum weight
    return k[n][W]

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