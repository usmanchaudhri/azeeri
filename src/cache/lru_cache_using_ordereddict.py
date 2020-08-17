from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # move this item to end of the dict since this will
            # be most recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            # if cache increases in capacity, pop the least used item
            self.cache.popitem(last=False)

if __name__ == "__main__":
    d = OrderedDict()
    d[1] = 'a'
    d[2] = 'b'
    d[3] = 'b'
    # d.move_to_end(1)
    print(d)

    # extracts item from the beginning
    print(d.popitem(last=False))

    # extracts the last item
    print(d.popitem())

