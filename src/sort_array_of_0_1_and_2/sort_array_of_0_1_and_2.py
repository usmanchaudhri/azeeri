"""
Given balls of these three colors (Red, Green and Blue) arranged randomly in a line (the actual. 8/18
number of balls does not matter), the task is to arrange them such that all balls of the same color are together and their
collective color groups are in the correct order (Red first, Green next and Blue last). These are the colors similar to
the Dutch National Flag, hence the name. This is a popular sorting problem.
Solution constraints
* Use array as your data-structure to represent the balls, not linked lists.
* Do this in ONE pass over the array - not two passes, just one pass
* Your solution can only use O(1) extra memory i.e. you have to do this in-place. (For Java/C#, it's okay to convert
incoming String to a character Array or a buffer/builder, but don't use any other memory for processing)
* Minimize the number of swaps.
Input: A string of letters, where each letter represents a ball with color. R = Red Ball, 'G' '= Green Ball. B = Blue Ball
Output: A string of letters, in sorted order
e.g.
Input: GBGGRBRG
Output: RRGGGGBB
"""
from collections import defaultdict

# time O(n) | space number of distinct colors in the array o(N)
def sortUsingCount(balls):
    # count the number of balls and than rearrange the original array
    # with the appropriate sorting order
    rearrangeBalls = defaultdict(int)
    for i in range(len(balls)):
        rearrangeBalls[balls[i]] +=1

    r = rearrangeBalls.get('R')
    g = rearrangeBalls.get('G')
    b = rearrangeBalls.get('B')

    i = 0
    while r > 0:
        balls[i] = 'R'
        r -=1
        i +=1

    while g > 0:
        balls[i] = 'G'
        g -=1
        i +=1

    while b > 0:
        balls[i] = 'B'
        b -=1
        i +=1

    print(balls)

"""
using mid as a pivot pointer we will compare mid to low and mid to high and sort appropriately.
all values which have a higher precedence than mid goes to the right of mid and all values
which have a lower precedence than mid goes to the left of mid.
"""
# time O(N) | space O(1)
def sortBallsByOrder(balls):
    low = 0
    mid = 0
    hi = len(balls) - 1

    while mid <= hi:
        if balls[mid] == 'R':
            balls[low], balls[mid] = balls[mid], balls[low]
            low +=1
            mid +=1
        elif balls[mid] == 'G':
            mid +=1
        else:
            balls[mid], balls[hi] = balls[hi], balls[mid]
            hi -=1
    return balls

if __name__ == "__main__":
    balls = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']
    # print(sortUsingCount(balls))
    print(sortBallsByOrder(balls))



