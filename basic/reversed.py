"""
prints array in reverse order
"""
array = [1,2,3,4,5,6]
for i in reversed(array):
    print(i)

words = ["this", "is", "a", "car"]
reverse_words = []
for i in reversed(words):
    reverse_words.append(i)
print(reverse_words)

sentence = "this is a car"
reverse_sentence = ""
for i in reversed(sentence):
    reverse_sentence = reverse_sentence + i
print(reverse_sentence)