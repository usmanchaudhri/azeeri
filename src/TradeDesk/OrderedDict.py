from collections import OrderedDict

class CacheItem:
    def __init__(self, key, value):
        self.key = key;
        self.value = value;

class CacheSet:
    def __init__(self):
        self.dict = OrderedDict()

cacheSet = CacheSet()
print(cacheSet)