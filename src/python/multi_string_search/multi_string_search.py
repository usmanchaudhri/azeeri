"""
We can build a suffix tree where each combination in the suffix tree will be constructed
"""

class SuffixTree:
    def __init__(self, string):
        self.root = {}              # each letter would than point to a chain of letters.
        self.endSymbol = '*'        # to identify a word we need to end the chain of letters using some symbols.
        self.populateSuffixTreeFrom(string)

    def populateSuffixTreeFrom(self, string):
        # for each letter build the suffix tree
        for i in range(len(string)):                        # traverse all n elements O(n)
            self.insertSuffixTreeStartingAt(i, string)

    def insertSuffixTreeStartingAt(self, i, string):
        """ every substring of the original string will be considered here and will be inserted into the
            suffix tree
         """
        node = self.root
        for j in range(i, len(string)):
            # check if j already does not exist at the root level
            letter = string[j]
            if letter not in node:
                # if the letter does not exits start a new trie chain
                node[letter] = {'*': True}

            # if the letter already exists in the trie chain than just traverse the next element in the trie
            # chain
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        # check whether the string exists in the Suffix tree.
        # start at the root
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]

        # last node returned here, check whether the last symbol in that Suffix chain
        # is a valid end symbol and return True if it is, False otherwise.
        return self.endSymbol in node

suffix = SuffixTree('3141592653589793238462643383279')
small_strings = ['314', '3', '65358', '222']
for string in small_strings:
    print(suffix.contains(string))


def put_spaces(pi_string, words):
    n = len(pi_string)
    for i in range(n):
        # 0, 1, 2, 3, 4, 5, 6
        check(i, pi_string, n)

def check(pos, pi_string, n):
    if pos == n:
        return 0

    prefix = ""
    ans = float("inf")
    for j in range(pos, n, 1):
        prefix += pi_string[j]
        if exist(prefix):
            other = check(j+1, pi_string, n)
            if other != -1:

                # the 1+ is to reflect that we can now add space here.
                ans = min(ans, 1+other)
    return ans

def exist(str):
    words = ['314', '3', '65358']
    words = set(words)
    if str in words:
        return True
    return False


# big_string = "3141592653589793238462643383279"
# strings = ['314', '3', '65358']
# strings = set(strings)

