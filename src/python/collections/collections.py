import collections

# Tally occurrences of words in a list
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] =+1
print(cnt)
print(type(cnt))


