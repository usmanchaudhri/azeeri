def calculateAverage(array):
    sum: int = 0
    for i in range(len(array)):
        sum = sum + array[i]
    print(sum/len(array))

# array = [1,2,3,4,5,6]
# calculateAverage(array)


"""
method 2
"""
def getAvg(currItem, itemCount, sum):
    sum = sum + currItem
    return float(sum) / itemCount

def streamAvg(arr, n):
    avg = 0
    sum = 0
    for i in range(n):
        itemCount = i+1
        avg = getAvg(arr[i], itemCount, sum)
        print('Avg %s', avg)

        sum = avg * itemCount
        print('Sum %s', sum)

array = [10, 20, 30, 40, 50]
n = len(array)
streamAvg(array, n)
