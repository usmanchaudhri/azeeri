
"""
[7, 2, 4, 6, 5, 9, 12, 11]
[2, 4, 5, 6, 7, 9, 11, 12]

[0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10]
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

0 +2+ 0 +  =  2
2 +2+ 2 + (1) = 7
7 +2+ 2

start from the beginning
jump 1 = 2
jump 2 = 2+2
jump 3 = 4+2
until it hits the end of the array

how will we reach to the end of the array with min number of steps given that each step is 2 slots.
"""

# [2, 4, 5, 6, 7, 9, 11, 12]
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# k = number of steps
def minNumOfTransmitters(houses, k):
    houses.sort()
    numOfTransmitters = 0

    i = 0
    n = len(houses) - 1
    # n = houses[-1]

    while i < n:
        # place the transmitter and calculate the position
        numOfTransmitters += 1

        # calculate the position where to place the first transmitter
        location = houses[i] + k

        # loop to the location where the transmitter will be placed.
        # skipping the locations to the left of transmitter
        while(i < n and houses[i] <= location):
            i +=1

        # i will be the location to place the transmitter
        # calculate the next location to place the transmitter
        i -=1
        location = houses[i]+k

        # now we find the location of the next transmitter
        # since the transmitter covers both <- and -> by 2 slots
        # we will now skip 2 slots to the right and
        while(i < n and houses[i] <= location):
            i+=1


    print(numOfTransmitters)

if __name__ == "__main__":
    houses = [7, 2, 4, 6, 5, 9, 12, 11]
    range = 2
    minNumOfTransmitters(houses, range)



