"""
Given an input string composed of opening and closing brackets, determine if the brackets
are balance.

input = "([])(){}(())()("

"""

def is_balance_brackets(input):
    opening_brackets = '([{'
    closing_brackets = ')]}'
    stack = []
    matching_brackets = {')': '(',
                         ']': '[',
                         '}': '{'}

    """
    traverse through each element in the input array
    # check if the character is an opening or closing bracket
    """
    for char in input:
        if char in opening_brackets:
            stack.append(char)
        if char in closing_brackets:
            if len(stack) == 0:
                return False

            if stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False

input = '([])(){}(())()('
print(is_balance_brackets(input))