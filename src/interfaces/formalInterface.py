from abc import ABC
from abc import abstractmethod

class Replacement(ABC):
    def __init__(self, data: dict):
        self.store: dict = data

    @abstractmethod
    def set(self, key, value):
        pass

    def get(self, key):
        return self.store.get(key)

class ReplacementMRU(Replacement):
    def __init__(self, data: dict):
        super().__init__(data)

    def set(self, key, value):
        self.store[key] = value

class ReplacementLRU(Replacement):
    def __init__(self, data: dict):
        super().__init__(data)

    def set(self, key, value):
        self.store[key] = value

if __name__ == "__main__":
    # data = {}
    # lru = ReplacementLRU(data)
    # lru.set('a', 10)
    #
    # mru = ReplacementMRU(data)
    # mru.set('b', 20)
    #
    # print(lru.get('a'))
    # print(mru.get('b'))
    # print('')

    from collections import OrderedDict
    oDict = OrderedDict()
    oDict['a'] = 10
    oDict['b'] = 20

    print(oDict)
    print('a' in oDict)













