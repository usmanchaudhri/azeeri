"""
You will be given a string representation of a number and a maximum number of changes you can make. Alter the string,
one digit at a time, to create the string representation of the largest number possible given the limit to the number
of changes. The length of the string may not be altered, so you must consider 0's leftIdx of all higher digits in your
tests. For example0110is valid, 0011is not.

Solution:
- first find how many different leftIdx and rightIdx corresponding characters we have - parse the array from
    leftIdx increasing and rightIdx decreasing order comparison.

- start from left (0) and right (len())
- character at leftIdx and rightIdx characters are equal and we have 2 change count left, then
    upgrade the value at leftIdx and rightIdx to 9 which is the highest digit value. Subtract the change couut
    by 2.

- character at leftIdx and rightIdx are not equal upgrade character at leftIdx an rightIdx only if they are not
    already set to '9'. Subtract the change count.

- character at leftIdx and rightIdx are not equal swap the higher value with the lower value which will make the
    character at leftIfx and rightIdx equal. Subtract 1 from change count.

"""
def highestValuePalindromeUsingKChanges(string, k):
    leftIdx = 0
    rightIdx = len(string) - 1
    diff = 0

    # find how many leftIdx and rightIdx corresponding characters are different
    while leftIdx <= rightIdx:
        if string[leftIdx] != string[rightIdx]:
            diff += 1
        leftIdx += 1
        rightIdx -= 1

    # if diff is greater than the number of changes constraint
    if diff > k:
        return '-1'

    leftIdx = 0
    rightIdx = len(string) - 1
    while rightIdx >= leftIdx:
        if k <= 0:
            # break loop when there are no change count left
            break

        if string[leftIdx] == string[rightIdx]:
            # if leftIdx and rightIdx are equal
            if k > 1 and (k-2) >= diff and string[leftIdx] != '9':
                string[leftIdx] = '9'
                string[rightIdx] = '9'
                k -= 2
        else:
            # if leftIdx and rightIdx are not equal
            # 5 and 7 - now we want to upgrade both 5 and 7 to the highest digit which is 9
            if k > 1 and (k-2) >= diff - 1:
                if string[leftIdx] != '9':
                    string[leftIdx] = '9'
                    k -= 1
                if string[rightIdx] != '9':
                    string[rightIdx] = '9'
                    k -= 1
            else:
                if string[leftIdx] > string[rightIdx]:
                    string[rightIdx] = string[leftIdx]
                else:
                    string[leftIdx] = string[rightIdx]
                k -= 1

            # diff reflects how many pairs are not palindromes
            diff -= 1

        # handle the case for the middle number in case there are odd numbers
        # check if we are in the middle index and the change count is > 0
        if leftIdx == rightIdx and k > 0:
            string[leftIdx] = '9'
            k -= 1

        leftIdx += 1
        rightIdx -= 1

    return ''.join([char for char in string]) if ispalindrome(string) else '-1'

def ispalindrome(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def split(word):
    return [char for char in word]

# print(ispalindrome('ababa'))
# k = split("3943")
k = split("092282")
result = highestValuePalindromeUsingKChanges(k, 3)
print(result)
# l = ['3', '9', '9', '3']
# result = str(''.join([i for i in l]))
# print(result)
















