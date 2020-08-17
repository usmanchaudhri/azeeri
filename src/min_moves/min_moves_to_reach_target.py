"""
Find minimum moves to reach target on an infinite line
Suppose we have a number position in infinite number line. (-inf to +inf). Starting from 0, we have to reach to the target by moving as described.
In ith move, we can go i steps either left or right. We have to find minimum number of moves that are required. Suppose the target is 2, so minimum
steps will be 3. From 0 to 1, from 1 to -1 and from -1 to 2.

To solve this problem, we have some important points to remember. If the target is negative, then just take this as positive, as the number line is
identical. For solving, the idea is move in one direction as long as possible. So from 0 go to 1, from 1 go to 3 (1 + 2), from 3 go to 6(1 + 2 + 3)
and so on. Thus if after nth move the target is found, then simply return the number of moves. But if the founded point is greater than target, then
we have to find the difference between how much we are ahead. Now we can see, if we move ith step backward, then the sum will be (sum – 2i). Now if sum-2i
is the target, then we have got the result. But the difference can be even or odd. For even, return n as result, otherwise, we take one more step.
So add n + 1 to sum and now again take the difference. If n + 1 is target, then return, otherwise do one more step with n + 2.
"""

def minStepToTarget(target):
    target = abs(target)

    sum = 0
    min_step = 0
    while sum < target or (sum - target) % 2 != 0:
        min_step = min_step + 1
        sum = sum + min_step

    return min_step

if __name__ == "__main__":
    print('')
    print(minStepToTarget(10))