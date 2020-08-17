"""

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def sortedArrayToBst(nums):
    tree = helper(nums, 0, len(nums)-1)
    print(tree)


def helper(nums, low, high):
    if low > high:
        return None

    mid = (low + high)//2

    # center val of sorted array as the root of the bst
    head = TreeNode(nums[mid])

    # left of the mid value should go to the left of this root node to satisfy bst
    head.left = helper(nums, low, mid-1)

    # right of the mid value should go to the right of this root node to satisfy bst
    head.right = helper(nums, mid+1, high)

    return head

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    sortedArrayToBst(nums)