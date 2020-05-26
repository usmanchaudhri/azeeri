"""
Check if an array can be divided into pairs whose sum is divisible by k.
Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs
such that sum of every pair is divisible by k.

Input: arr[] = {9, 7, 5, 3},
k = 6
Output: True
We can divide array into (9, 3) and
(7, 5). Sum of both of these pairs
is a multiple of 6.

Note:
    - if the sum of two numbers is divisible by K than the numbers are divisible by K
    - 14 is divisible by 7, because 14 / 7 = 2 exactly
    - 15 is not divisible by 7, becuase 15 / 7 = 2(1/7) (the result is now a whole number)

Solution-1:

Solution-2:

"""

def divisiblePairs(array, k):
    # if length of array is odd than odd cannot be divided into pairs
    if not isEven(len(array)):
        return False

    remainders = []
    for element in array:
        rem = element % k
        remainders.append(rem)
    print(remainders)


def isEven(num):
    return (num%2) == 0

if __name__ == "__main__":
    array = [9, 7, 5, 3]
    divisiblePairs(array, 6)

    # print(3%6)
    # print(6%3)
    # print(3/6)
    # print(6/3)

