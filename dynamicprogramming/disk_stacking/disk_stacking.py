"""
You're given a non-empty array of arrays where each subarray holds three integers and represents a disk. These
integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to
maximize the total height of the stack. A disk must have a strictly smaller width, depth, and height than any other
disk below it.

Write a function that returns an array of the disks in the final stack, starting with the top disk and ending
with the bottom disk. Note that you can't rotate disk; in other words, the integers in each subarray must
represent [width, depth, height] at all times.

You can assume that there will only be one stack with the greatest total height.

disks  = [[2,1,2], [3,2,3], [2,2,8], [2,3,4], [1,3,1], [4,4,5]]
output = [[2,1,2], [3,2,3], [4,4,5]]
"""

"""
Solution:
- sort the disk by height, so, we know that each successive disk's height in the array is greater than the previous 
disk.
- use dynamic programming to calculate the max stackable disk height at the current index given the constraints
the the width and depth of the bottom disk should be greater than the disk on the top.
- return the set of stacked disks which has the maximum height and than build the sequence of stacked disks
from there. 
"""
def diskStacking(disks):
    # The question asks to find stackable disks by the tallest height, so, we will just sort the input array
    # by height and than use dynamic programming to than calculate max heights at each disk location
    disks.sort(key = lambda disk: disk[2])

    # use the heights array to track max height at each disk location
    heights = [disk[2] for disk in disks]

    # this will build the sequences array which will hold the sequence of disks for
    # the tallest (using height) tower
    sequences = [None for disk in disks]

    # keeps track of the max height index in the heights array
    maxHeightIdx = 0

    # program execution, we will use dynamic programming to check all possible stackable disks
    # at each location of disks array. And we will find out what is the max height at each successively
    # location in the heights array.
    # Finally we will build a sequence of disk arrays and the max height of a sequence which has
    # the maximum height.
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] <= currentDisk[2] + heights[j]
                    sequences[i] = j

        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i
    return buildSequence(disks, sequences, maxHeightIdx)

def areValidDimensions(o, c):
    # these are the constraints for stacking one disk over another.
    # this the weight, depth, and height of the bottom disk has to be greater than the
    # weight, depth, and height of the top disk.
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSequence(array, sequences, currentIdx):
    # at this point we have the sequences which is the disks involved to make-up the tallest
    # stack. Now we have to build the sequence and return the actual disks back.
    sequence = []
    while currentIdx is not None:   # the None here refers back to where we initialize the sequences with None
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

if __name__ == "__main__":
    disks  = [[2,1,2], [3,2,3], [2,2,8], [2,3,4], [1,3,1], [4,4,5]]
    diskStacking(disks)



















