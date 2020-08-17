
class PrefixTree(object):
    def __init__(self, letter=None):
        self.letter = letter
        self.children: {} = {}
        self.stop = False

    def add(self, word):
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = PrefixTree(letter)
            return self.children[letter].add(word)
        else:
            self.stop = True
            return self

    def find_letter(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]

    def __repr__(self):
        return "PrefixTree(letter={0}, stop={1})".format(self.letter, self.stop)

if __name__ == "__main__":
    prefixTree = PrefixTree()
    prefixTree.add("abbbccd")
    print(prefixTree)
    # prefixTree.find_letter("cd")

