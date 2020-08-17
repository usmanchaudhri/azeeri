from collections import defaultdict



if __name__ == "__main__":
    # x = dict()
    # x['one'] = 1
    # print(x)
    # print(x.get('one', 'default'))
    t = [defaultdict(str) for i in range(3)]
    t[0]['a'] = 1
    t[0]['b'] = 2
    t[1]['c'] = 3
    t[1]['d'] = 4
    t[2]['e'] = 5
    t[2]['f'] = 6
    print(t)