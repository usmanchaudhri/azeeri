
# O nlog(n)
def min_loss(price):
    myDict = {}
    for i in range(len(price)):
        myDict[price[i]] = i
    print(myDict)

    # housePrice = price[:]
    # housePrice.sort()
    # minCost = float("inf")      # a very large number
    # for i in range(1, len(prices)):
    #     if ((housePrice[i]-housePrice[i-1]) < minCost and price[i] < price[i-1]):
    #         minCost = housePrice[i]-housePrice[i-1]
    #
    # print(minCost)

if __name__ == "__main__":
    # prices = [20, 15, 8, 2, 12]
    prices = [5, 10, 3]
    years = 5
    min_loss(prices)