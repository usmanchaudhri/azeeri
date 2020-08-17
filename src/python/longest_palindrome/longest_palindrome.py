
"""
abaxyzzyxf
-   aba -> odd combination - start at b and check both letters previous and next to b
-   ab  -> even combination - the letter to left and the current letter for palindrome
"""
# O(n^2) time | O(1) space
def longestPalinDrome(string):
    # we will store the current longest substring - starting and ending index.
    currLongest = [0,1]

    # we know that the first letter is a palindrome so start from index 1
    for i in range(1, len(string)):
        # for each letter we will expand in both ways - right and left and
        # keep expanding for valid palindrome
        # we have to find the odd and even palindromes
        odd = getLongestPalindrome(string, i-1, i+1)
        even = getLongestPalindrome(string, i-1, i)

        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currLongest = max(longest, currLongest, key = lambda x: x[1] - x[0])

    # we are doing currLongest[1]+1 since when slicing string index the right index is exclusive
    return string[currLongest[0]: currLongest[1]+1]

def getLongestPalindrome(string, left_idx, right_idx):

    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break

        # move pointers left and right for the next characters
        left_idx -= 1
        right_idx += 1

    # for both the while and if condition when the loop breaks we will be one position far to the left
    # and one position far to the right. We would then return the previous left_idx which will be
    # left_idx+1 and one previous right index which will be right_idx-1. However in our currLongest string
    # the right index we have is one greater than the current right index [0,1]
    return [left_idx+1, right_idx+1]



longestPalinDrome("abaxyzzyxf")

