
# def valid_sentence(string, dictionary) -> bool:
#     words = string.split(' ')
#     words.sort(key=lambda x: str(x))
#     dictionary.sort(key=lambda x: str(x))
#
#     for i in range(len(words)):
#         if words[i] != dictionary[i]:
#             return False
#     return True

from collections import defaultdict

def valid_sentence(string, dictionary):
    # sdict = set(dictionary)
    sdict = defaultdict(int)
    for word in dictionary:
        # sdict[word] += 1
        sdict[word] += 1

    if "practice" in sdict:
        print("practice exits")

string = "Practice makes perfect."
dictionary = ['practice', 'perfect', 'makes']

# the dictionary could be very big so sort the dictionary at the loading time
valid_sentence(string, dictionary)
