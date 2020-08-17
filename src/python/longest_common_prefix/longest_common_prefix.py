"""
Give a set of words (Array of strings) find largest common prefix.
['Apple', 'App', 'Application', 'April', 'Api']

Ap ple
Ap p

Ap plication
Ap ril
Ap i

Step 1 : find the shortest string in the array and let this length be L
"""

def findMinLength(array):
    return len(min(array, key=len))

def ifAllContainsPrefix(words, str, start, end):
    """
    compare the words - individual character at a time.
    """
    for i in range(0, len(words)): # for each word in the list
        word = words[i]
        for j in range(start, end+1):
            if word[j] != str[j]:
                return False
    return True

def longestCommonPrefix(words):
    index = findMinLength(words)

    prefix = ""

    left = 0
    right = index - 1

    while left <= right:
        mid = (left + right)//2
        # check if all the strings in the list contains the current prefix
        # the prefix is calculated as the LENGTH of the smallest string
        # in the list of words.
        if ifAllContainsPrefix(words, words[0], left, mid):

            # if all the strings in the input array
            # contains this prefix then append this
            # substring to our answer
            prefix = prefix + words[0][left : mid+1]

            # go for the right part
            left = mid + 1
        else:

            # go for the left part
            right = mid - 1

    return prefix

if __name__ == "__main__":
    words = ['Apple', 'App', 'Application', 'April', 'Api']
    lcp = longestCommonPrefix(words)
    print(lcp)

    # print(words[0][1:4])