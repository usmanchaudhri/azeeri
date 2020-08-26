"""
Product of array except self
"""

def product_except_self(nums):
    ans = [1] * len(nums)
    print(ans)

    totalProd = 1
    for i, x in enumerate(nums):
        ans[i] = totalProd
        totalProd *= x


nums = [1, 2, 3, 4]
product_except_self(nums)