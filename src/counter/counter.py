from collections import Counter
from collections import defaultdict

if __name__ == "__main__":
    c = Counter('usman')

    c = Counter()
    c['a'] += 1
    c['a'] += 1
    c['b'] += 3
    # print(c)
    # print(list(c.elements()))
    # print(list(c.most_common(1)))

    d = defaultdict(int)
    d['a'] += 0
    d['b'] += 1
    # print(d)

    s = set()
    s.add(1)
    s.add(2)
    # print(s)

    d = {}
    d['1'] = 10
    d['1'].value = 20
    print(d)

