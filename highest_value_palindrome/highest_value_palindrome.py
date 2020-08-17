"""
You will be given a string representation of a number and a maximum number of changes you can make. Alter the string,
one digit at a time, to create the string representation of the largest number possible given the limit to the number
of changes. The length of the string may not be altered, so you must consider 0's left of all higher digits in your
tests. For example0110is valid, 0011is not.

Shortcut Ctrl + Command + G for selecting similar occurrences
"""
def highestPalindromeUsingKChanges(string, k):
    left = 0
    right = len(string) - 1
    diff = 0

    while left <= right:
        if string[left] != string[right]:
            diff += 1
        left += 1
        right -= 1

    if diff > k:
        return -1

    while right >= left:
        if k <= 0:
            return -1

        if string[left] == string[right]:
            # if we replace both values with the highest integer value and are within the
            # limits of number of changes we can do
            if k > 1 and (k-2) >= diff and string[left] != '9':
                string[left] = '9'
                string[right] = '9'
                k -= 2

        else:
            if k > 1 and (k-2) >= diff - 1:
                if string[left] != '9':
                    string[left] = '9'
                    k -= 1
                if string[right] != '9':
                    string[right] = '9'
                    k -= 1
            else:
                if string[left] > string[right]:
                    string[right] = string[left]
                else:
                    string[left] = string[right]
                k -= 1
            diff -= 1   # diff reflects how many pairs are not equal to each other

        # handle the case for the middle number in-case the list has odd number of values
        # also check if we have any change count left
        if left == right and k > 0:
            string[left] = '9'
            k -=1

        left += 1
        right -= 1

    return string if isPalindrome(string) else -1

def isPalindrome (string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


res = highestPalindromeUsingKChanges('3943', 1)
print(res)
