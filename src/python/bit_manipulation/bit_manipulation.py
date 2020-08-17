"""
4 ->  100
7 ->  111
"""

# shift left
# multiply 2 by 2^2
x = 2 << 1
# print(x)

# divide 2 by 2^2
x = 2 >> 3
# print(x)

x = 4 ^ 7 ^ 7
# print(x)
#
# res = "{0:b}".format(4)
# print(res)
# res = "{0:b}".format(7)
# print(res)

n = 10
n = n & (n-1)
# print(10 & 8)
# 1010  (10)
# 0111  (7)
# 0010  (2)

# to determine if a number is power of 2
# 1010  (10)
# 1000  (8)
# 1000  (8)

"""
Using bit manipulation we can determine if a given number is a power of 2.
For a given number n i.e 10 we will do a bitwise and with 

10 & 9 doing a bitwise (&) will give the number which is power of 2. 
Compare the result of 10 & 9 to the given number and if they are equal than the
given number is a power of 2. 
"""
def is_pow_2(n):
    return n & (n & (n-1)) == 0

def set_bits(n):
    count = 0
    while n:
        n = n & (n-1)
        count +=1
    return count

# res = set_bits(10)
# print(res)

print(10 & 1)

# 001
# 100
# 000

# print(is_pow_2(134))
# print(is_pow_2(128))
# print(is_pow_2(130))







