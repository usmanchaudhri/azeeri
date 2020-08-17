"""
Used in cases for finding strings, matching strings
In Suffix Trie the tree will contain all possible suffixes for the current letter
{a: {b: {b: {b: {c: {c: {d}}}}}}} implies a-> bbbccd
b->bbccd
b->bccd
b->ccd
c->cd
c->d
d
"""
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTreeFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTreeFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    # O(m) time | O(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node

# class SuffixTrie:
#     def __init__(self, string):
#         self.root = {}
#         self.endSymbol = "*"
#         self.populateSuffixTreeFrom(string)
#
#     def populateSuffixTreeFrom(self, string):
#         for i in range(len(string)):
#             self.insertSubstringStartingAt(i, string)
#
#     def insertSubstringStartingAt(self, i, string):
#         node = self.root
#         for j in range(i, len(string)):
#             letter = string[j]
#             if letter not in node:
#                 node[letter] = {}
#             node = node[letter]
#         node[self.endSymbol] = True


if __name__ == "__main__":
    # map = {}
    # map['*'] = True
    # print(map['*'])
    tree = SuffixTrie('abbbccd')
    # tree.populateSuffixTreeFrom("cd")
    print(tree.contains("cd"))
