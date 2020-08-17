"""

"""
def shortest_chain_length(start, target, word_list):
    # words = set(word_list)
    queue = []
    transitions = 0

    if target not in word_list:
        # if the target word is not in the dictionary
        return 0

    # push the starting word into the queue
    queue.append(start)
    while queue:
        # remove the first word from the queue
        curr_word = queue.pop(0)

        print(curr_word, end=' -> ')

        # traverse all the words in the list which are one character different than
        # the current word.
        i = 0
        while i < len(word_list):
            word = word_list[i]
            if differ_by_one(word, curr_word):
                queue.append(word)
                transitions += 1
                del word_list[i]

                # we have found the answer and so return the number of transitions
                if word == target:
                    print(word)
                    return transitions
            i += 1

    return 0

def differ_by_one(word1, word2):
    length = len(word1)
    count = 0
    for i in range(length):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False

    if count == 1:
        return True

    return False


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print('Number of transitions: ', shortest_chain_length(beginWord, endWord, wordList))

# words = ['cot', 'hot', 'lot']
# i = 0
# while i < len(words):
#     element = words[i]
#     if True:
#         del words[i]
#         print(words)
