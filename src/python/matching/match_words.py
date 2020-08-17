from collections import defaultdict

def match(words, word):
    res = sorted(word)
    for wor in words:           # O (n)
        temp = sorted(wor)      # O nlogn
        if res == temp:
            print('we can form word', wor)

word = "using"
words = ["suing", "uses", "gaining"]
# match(words, word)

word = "using"
temp = defaultdict(int)

for element in word:
    temp[element] += 1
print(temp)

word2 = "suing"
for element in word2:
    temp[element] -= 1
print(temp)
res = all(v == 0 for v in temp.values())
print(res)