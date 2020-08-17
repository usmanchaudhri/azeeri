"""
Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of . If it is,
they divide it by . If not, they reduce it by the next lower number which is a power of . Whoever reduces the number
to  wins the game. Louise always starts.

Given an initial value, determine who wins the game.

As an example, let the initial value . It's Louise's turn so she first determines that  is not a power of . The next
lower power of  is , so she subtracts that from  and passes  to Richard.  is a power of , so Richard divides it by
and passes  to Louise. Likewise,  is a power so she divides it by  and reaches . She wins the game.

Update If they initially set counter to , Richard wins. Louise cannot make a move so she loses.

"""

import math
from queue import Queue
from collections import deque
"""
both richard an louise will run one step at a time.
- Richard and Louise are playing the game
- put richard and louise in a queue which we will keep replacing the top with each step
"""
def counterGame(n):
    players = deque()
    players.append('Louise')
    players.append('Richard')


    # check if is power of 2
    if isPowerOfTwo(n):
        power = n // 2
        execute(power)
    else:
        # not a power of
        power = nextLowerPowerOfTwo(n)
        power = n - power
        players.append(players.popleft())
        execute(power, players)


"""
divide and split among the two
"""
def execute(number, players):
    pass

def isPowerOfTwo(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

def nextLowerPowerOfTwo(n):
    while n != 1:
        if math.ceil(math.log2(n)) == math.floor(math.log2(n)):
            return n
        n -=1

n = 132
counterGame(n)

res = "{0:b}".format(132)
print(res)
# print(type(bin(132)))


# print("{0:b}".format(18))
# print(isPowerOfTwo(n))
# powerOfTwo = nextLowerPowerOfTwo(n-1)
# print(powerOfTwo)
# print(pow(132, 2))
# find next power of 2
# next = pow(2, math.ceil(math.log(66) / math.log(2)))
# print(next)