
def recursion_with_loop(array):
    helper(0, array)

def helper(i, array):
    for j in range(i, len(array)):
        print('before j to i ', j, i)
        helper(i+1, array)
        print('after j to i ', j, i)

recursion_with_loop([1,2,3])