"""
Short Palindrome

Consider a string, , of  lowercase English letters where each character,  (, denotes the letter at index  in .
We define an  palindromic tuple of  to be a sequence of indices in  satisfying the following criteria:

a k a k a k
"""
# O(n^3) time | O(n^2) space
def palindromePartitionMinCuts(string):
    palindromes = [[False for i in string] for j in string]

    # builds a two dimensional array which lists all possible strings
    # starting from index 0 to length of the string.
    # Row = starting index and Col = ending index
    # (0, 3) - string starting from 0 index to 3
    for i in range(len(string)):
        for j in range(len(string)):
            palindromes[i][j] = isPalindrome(string[i:j+1])

    # min number of cuts
    cuts = [float("inf") for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            # if the string is not a palindrome than exclude the current character
            # and put a cut right before the current character
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
    return cuts[-1]

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

def palindromePartition(string):
    # two-dimensional array row is the starting index and column is the ending index.
    palindromes = [[False for i in string] for j in string]

    # this is the diagonal of the matrix and it will be
    for i in range(len(string)):
        palindromes[i][i] = True

    for length in range(2, len(string) + 1):
        """
        string = akakak
        range(2, 5+1)
        length = 2  
            range(0, 5 - 2 + 1) => range(0, 4)
                j = 0 + 6 - 1   => 5                                
        """
        for i in range(0, len(string) - length + 1):
            """
            length = 2      range(0, 5 - 2+1)
            i = 0, 1, 3, 4
            j = 1, 2, 4, 5
            
            length = 3      range(0, 5 - 3+1)   =>  range(0, 1)
            i =
            
            length = 4      range(0, 5 - 4+1)   =>  range(0, 0)   
             
             
            length = 5      range(0, 5 - 5+1)   =>  range(0, -1)
             
            
            length = 6      range(0, 5 - 6+1)
             
            """
            j = i + length - 1
            if length == 2:
                # if the length is 2 than the only thing we are checking is
                # if the two characters are equal or not.
                palindromes[i][j] = string[i] == string[j]
            else:
                # if the length is greater than 2 than check if the outer most characters are equal
                # also check if the inner character are equal too.
                palindromes[i][j] = string[i] == string[j] and palindromes[i+1][j-1]


if __name__ == "__main__":
    s = "akakak"
