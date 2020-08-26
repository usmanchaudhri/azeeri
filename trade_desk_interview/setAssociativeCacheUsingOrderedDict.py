from __future__ import print_function
from collections import OrderedDict
import sys;

class FormatError(Exception):
    pass

def main():
    SetAssociativeCacheRunner.parseInput(sys.stdin);

file_print = eval('print')


'''
Parses Test Case input to instantiate and invoke a SetAssociativeCache
NOTE: You can typically ignore anything in here. Feel free to collapse...
'''
class SetAssociativeCacheRunner:
    @staticmethod
    def parseInput(reader):
        replacementAlgoName = None;
        cache = None;

        # Process each line in the input.
        line = reader.readline().strip();
        (cache, replacementAlgoName) = SetAssociativeCacheRunner.createCache(line);

        lineCount = 0;
        while True:
            lineCount += 1;
            try:
                # Read next line
                line = reader.readline().strip();
                if line == None or len(line) == 0:
                    break;

                # All remaining lines invoke instance methods on the SetAssociativeCache
                retValue = SetAssociativeCacheFactory.invokeCacheMethod(line, cache);

                # Write the method's return value (if any) to stdout
                if retValue == None:
                    continue
                if type(retValue) == bool:
                    retValue = str(retValue).lower();

                file_print(retValue, file = sys.stdout);

            except KeyError as kerr:
                raise kerr;
            except Exception as ex:
                raise FormatError("Invalid test case input at line %d. Cannot parse '%s': %s" % (lineCount, line, ex));

    @staticmethod
    def createCache(inputLine):
        cacheParams = [item.strip() for item in inputLine.split(',')]
        setCount = int(cacheParams[0]);
        setSize = int(cacheParams[1]);
        replacementAlgoName = cacheParams[2];

        cache = SetAssociativeCacheFactory.createCache(setCount, setSize, replacementAlgoName);
        return (cache, replacementAlgoName);

############################ BEGIN Solution Classes ############################
# NOTE: You are free to modify anything below, except for class names and generic interface.
# Other public interface changes may require updating one or more of the helper classes above
# for test cases to run and pass.

'''
A Set-Associative Cache data structure with fixed capacity.

- Data is structured into `setCount` # of `setSize`-sized sets.
- Every possible key is associated with exactly one set via a hashing algorightm
- If more items are added to a set than it has capacity for (i.e. > `setSize` items),
  a replacement victim is chosen from that set using an LRU algorighm.

NOTE: Part of the exercise is to allow for different kinds of replacement algorithms...

Solution:
- For caches the put and get operations should be faster.
- The cache should not dependent on specific implementation of LRU or MRU

Issues:
- The cache uses set 

'''
class SetAssociativeCache:
    def __init__(self, setCount, setSize, replacementAlgo):
        self._replacementAlgo: IReplacementAlgo = replacementAlgo
        self._setSize = setSize;
        self._setCount = setCount;
        self._capacity = setCount * setSize;
        self._sets = [OrderedDict() for i in range(setCount)]   # OrderedDict() for storing cache items

    def capacity(self):
        return self._capacity;

    def setSize(self):
        return self._setSize;

    def setCount(self):
        return self._setCount;

    '''
    Gets the value associated with `key`. Throws if key not found.
    '''
    def get(self, key):
        setIndex = self._getSetIndex(key);
        currDict = self._sets[setIndex]
        return self._replacementAlgo.get(key, currDict)

    '''
    Adds the `key` to the cache with the associated value, or overwrites the existing key. 
    If adding would exceed capacity, an existing key is chosen to replace using an LRU algorithm
    (NOTE: It is part of self.exercise to allow for more replacement algos)
    '''
    def set(self, key, value):
        # calculate the desired dict index
        setIndex = self._getSetIndex(key)
        currDict = self._sets[setIndex]
        self._replacementAlgo.set(key, value, currDict)

    '''
    Returns `true` if the given `key` is present in the set; otherwise, `false`.
    '''
    def containsKey(self, key):
        setIndex = self._getSetIndex(key);
        currDict = self._sets[setIndex]

        # returns True if the key exits, False otherwise.
        return key in currDict

    '''
    Returns the count of items in the cache
    '''
    def count(self):
        return sum([len(set) for set in self._sets])

    '''
    Maps a key to a set
    '''
    def _getSetIndex(self, key):
        c = 2^31 - 1
        s = -1
        for i in range(len(self._sets)):
            if key in self._sets[i]:
                return i
            if len(self._sets[i]) < c:
                c = len(self._sets[i])
                s = i
        return s

'''
A common interface for replacement algos, which decide which item in a CacheSet to evict
'''
from abc import abstractmethod
from abc import ABC

class IReplacementAlgo(ABC):
    def __init__(self, capacity):
        self.capacity = capacity

    @abstractmethod
    def set(self, key, value, data):
        pass

    def get(self, key, store):
        if key not in store:
            raise KeyError("The key '%s' was not found" % key);
        else:
            store.move_to_end(key)
            return store[key]

class LRUReplacementAlgo(IReplacementAlgo):
    NAME = "LRUReplacementAlgo"

    def __init__(self, capacity):
        super().__init__(capacity)

    def set(self, key, value, store):
        store[key] = value
        store.move_to_end(key)
        if len(store) >= self.capacity:
            # for LRU move to the end
            store.popitem(last=False)

class MRUReplacementAlgo(IReplacementAlgo):
    NAME = "MRUReplacementAlgo"

    def __init__(self, capacity):
        super().__init__(capacity)

    def set(self, key, value, store):
        store[key] = value
        store.move_to_end(key)
        if len(store) >= self.capacity:
            # for MRU move to the end
            store.popitem(last=True)


# ^^ ######################### END Solution Classes ######################### ^^


'''
############################ BEGIN Helper Classes ############################
NOTE: Your code in the classes below will not be evaluated as part of the exericse.  
They are just used by the stub code in the header to help run HackerRank test cases. 
You may need to make small modifications to these classes, depending on your interface design, 
for tests to run and pass, but it is not a core part of the exercise
'''

'''
Cache factory helper class
'''
class SetAssociativeCacheFactory:
    '''
    NOTE: `replacementAlgoName` is provided in case you need it here. Whether you do will depend on your interface design.
    '''
    @staticmethod
    def createCache(setCount, setSize, replacementAlgoName):

        # TODO implement algo
        algo = ReplacementAlgoFactory.createReplacementAlgo("MRUReplacementAlgo", setCount * setSize);

        return SetAssociativeCache(setCount, setSize, algo);

    '''
    NOTE: Modify only if you change the main interface of SetAssociativeCache
    '''
    @staticmethod
    def invokeCacheMethod(inputLine, cacheInstance):
        # return inputLine;

        callArgs = [ item.strip() for item in inputLine.split(',') ];
        methodName = callArgs[0].lower();

        if methodName == "get":
            return cacheInstance.get(callArgs[1]);
        elif methodName == "set":
            cacheInstance.set(callArgs[1], callArgs[2]);
            return None;
        elif methodName == "containskey":
            return cacheInstance.containsKey(callArgs[1]);
        elif methodName == "getcount":
            return cacheInstance.count();
        else:
            # TODO: If you want to add and test other public methods to SetAssociativeCache,
            # add them to the switch statement here... (self.is not common)
            raise FormatError("Unknown method name '%s'" % methodName);


'''
// TODO: Consider making use of self.in the `SetAssociativeCacheFactory` above to map replacement algo name 
// to a IReplacementAlgo instance for the interface you design
'''

class ReplacementAlgoFactory:
    @staticmethod
    def createReplacementAlgo(replacementAlgoName, capacity):
        if replacementAlgoName == LRUReplacementAlgo.NAME:
            return LRUReplacementAlgo(capacity);
        elif replacementAlgoName == MRUReplacementAlgo.NAME:
            return MRUReplacementAlgo(capacity);
        else:
            raise FormatError("Unknown replacement algo '%s'" % replacementAlgoName);

# ^^ ######################### END Helper Classes ######################### ^^
# ^^ ######################### BEGIN FOOTER ############################### ^^


if __name__ == "__main__":
    # file = open('input000.txt')
    file = open('input009.txt')
    run = SetAssociativeCacheRunner()
    print(run.parseInput(file))