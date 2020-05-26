"""
Manual One Hot Encoded

In this example, we will assume the case where we have an example string of characters of alphabet letters, but the
example sequence does not cover all possible examples.

We will use the input sequence of the following characters: hello world

We will assume that the universe of all possible inputs is the complete alphabet of lower case characters,
and space. We will therefore use this as an excuse to demonstrate how to roll our own one hot encoding.

"""
from numpy import argmax

def onehot_encoded(data):
    # define input string
    # data = "hello world"
    print(data)

    # define universe of possible input value - include space( ) too.
    alphabet = 'abcdefghijklmnopqrstuvwxyz '

    # define a mapping of characters to integers for universe in this case
    # all alphabets
    char_to_int = dict((c,i) for i, c in enumerate(alphabet))
    int_to_char = dict((i,c) for i, c in enumerate(alphabet))

    # integer encode input data - this is the integer value
    # of each character in the input data
    integer_encode = [char_to_int[char] for char in data]
    print(integer_encode)

    # one hot encode
    onehot_encode = list()
    for value in integer_encode:
        letter = [0 for _ in range(len(alphabet))]
        letter[value] = 1
        onehot_encode.append(letter)
    print(onehot_encode)

    # invert encoding
    inverted = int_to_char[argmax(onehot_encode[0])]
    print(inverted)

if __name__ == "__main__":
    onehot_encoded("hello world")

    # print(argmax([0,0,9,7,5]))