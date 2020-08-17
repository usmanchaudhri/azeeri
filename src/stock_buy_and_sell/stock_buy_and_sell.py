"""
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in
those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by
buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in
decreasing order, then profit cannot be earned at all.

a better approach to solve this problem
- find the local minima and store it as the starting index
- find the local maxima and store it as the ending index. If we reach the end, set the end as ending index.
- update the solution - increment count of buy sell pairs.
- repeat the above steps if end is not reached.

Note: the local minima and maxima are two extremes within a given interval. The reason it is local maxima and minima
is because we are taking a sub-interval.

Explanation:
price = [100, 180, 260, 310, 40, 535, 695]
- if we take a look at the price array we would notice the increasing intervals in the array:
100 - 310 and 40 - 695. We have to identify the increasing intervals and keep track of the min value
and max value at that interval.
"""
# O(n) time | space constant
def stockBuySell(price, n):

    if n == 1:
        return

    # traverse through given price array
    buySell = []
    i = 0
    while i < n-1:
        # find local minima
        # note that the limit is (n-2) as we are
        # comparing present element to the next element
        # traverse through the sub array and find the increasing
        # elements starting and ending points
        while i < n-1 and price[i+1] <= price[i]:
            i +=1

        if i == n-1:
            break

        # store the index of minima
        buy = i
        i += 1

        # find local maxima
        # note that the limit is (n-1) as we are
        # comparing to previous element
        # Comparison - we compare to the previous element
        # to make sure we traverse to the end of the array.
        while i < n and price[i] >= price[i - 1]:
            i +=1

        # store the index of maxima
        sell = i-1

        print("Buy on day: ", buy, "Sell on day: ", sell)
        buySell.append([buy, sell])

    return buySell

if __name__ == "__main__":
    price = [100, 180, 260, 310, 40, 535, 695]
    price.sort(reverse=True)
    n = len(price)
    print(stockBuySell(price, n))

    # sell = []
    # sell.append([1])
    # print(sell)
