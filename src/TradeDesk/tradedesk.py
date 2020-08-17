from __future__ import print_function
from collections import deque;
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
                    continue;
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
'''
class SetAssociativeCache:
    def __init__(self, setCount, setSize):
        self._setSize = setSize;
        self._setCount = setCount;
        self._capacity = setCount * setSize;
        self._sets = [ CacheSet(setSize) for i in range(setCount) ];

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
        return self._sets[ setIndex ].get(key);

    '''
    Adds the `key` to the cache with the associated value, or overwrites the existing key. 
    If adding would exceed capacity, an existing key is chosen to replace using an LRU algorithm
    (NOTE: It is part of self.exercise to allow for more replacement algos)
    '''
    def set(self, key, value):
        setIndex = self._getSetIndex(key);
        self._sets[setIndex].set(key, value);

    '''
    Returns `true` if the given `key` is present in the set; otherwise, `false`.
    '''
    def containsKey(self, key):
        setIndex = self._getSetIndex(key);
        return self._sets[setIndex].containsKey(key);

    '''
    Returns the count of items in the cache
    '''
    def count(self):
        return sum([set.count() for set in self._sets]);

    '''
    Maps a key to a set
    '''
    def _getSetIndex(self, key):
        c = 2^31 - 1
        s = -1;
        for i in range(len(self._sets)):
            if self._sets[i].containsKey(key):
                return i;
            if self._sets[i].count() < c:
                c = self._sets[ i ].count();
                s = i;
        return s;

'''
An internal data structure representing one set in a N-Way Set-Associative Cache
'''
from collections import OrderedDict
class CacheSet:
    # why cannot we use dict here since
    def __init__(self, capacity):
        # self._count = 0;
        # self._usageTracker = deque();
        self._capacity = capacity;
        self._store = OrderedDict()
        # self._store = [ None for i in range(capacity) ];

    def count(self):
        return self._count;

    def capacity(self):
        return self._capacity;

    '''
    Gets the value associated with `key`. Throws if key not found.
    '''
    def get(self, key):
        if key not in self._store:
            raise KeyError("The key '%s' was not found" % key);
        else:
            self._store.move_to_end(key)
            return self._store[key]

        # if self._store containsKey(key):
        #     self._recordUsage(key);
        # else:
        #     raise KeyError("The key '%s' was not found" % key);
        #
        # return self._store[self._findIndexOfKey(key)].value;

    '''
    Adds the `key` to the cache with the associated value, or overwrites the existing key. 
    If adding would exceed capacity, an existing key is chosen to replace using an LRU algorithm
    (NOTE: It is part of self.exercise to allow for more replacement algos)
    '''
    def set(self, key, value):
        self._store[key] = value
        self._store.move_to_end(key)
        if len(self._store) >= self._capacity:
            # if cache increases in capacity, pop the least used item
            # here we can determine which algorithm to use - LRU or MRU
            self._store.popitem(last=False)

        # indexOfKey = self._findIndexOfKey(key);
        #
        # if indexOfKey >= 0:
        #     self._store[indexOfKey].value = value;
        # else:
        #     indexToSet = None;
        #     # If the set is at it's capacty
        #     if self._count == self._capacity:
        #         # Choose the Least-Recently-Used (LRU) item to replace, which will be at the tail of the usage tracker
        #         # TODO: Factor self.logic out to allow for custom replacement algos
        #         keyToReplace = self._usageTracker[-1];
        #         indexToSet = self._findIndexOfKey(keyToReplace);
        #
        #         # Remove the existing key
        #         self._removeKey(keyToReplace);
        #     else:
        #         indexToSet = self._count;
        #
        #     self._store[indexToSet] = CacheItem(key, value);
        #     self._count += 1;
        #
        # self._recordUsage(key);

    '''
    Returns `true` if the given `key` is present in the set; otherwise, `false`.
    '''
    def containsKey(self, key):
        if key not in self._store:
            return -1
        else:
            return self._store[key]

        # return self._findIndexOfKey(key) >= 0;

    def _removeKey(self, key):
        if key not in self._store:
            return
        else:
            del self._store[key]

        # indexOfKey = self._findIndexOfKey(key);
        # if indexOfKey >= 0:
        #     self._usageTracker.remove(key);
        #     self._store[indexOfKey] = None;
        #     self._count -= 1;

    # def _findIndexOfKey(self, key):
    #     # key should be a direct set lookup
    #     for i in range(self._count):
    #         if self._store[i] != None and self._store[i].key == key:
    #             return i;
    #     return -1;

    # def _recordUsage(self, key):
    #     try:
    #         self._usageTracker.remove(key);
    #     except ValueError:
    #         # Ignore if value not existing
    #         pass
    #     self._usageTracker.appendleft(key);

'''
An internal data structure representing a single item in an N-Way Set-Associative Cache
'''
class CacheItem:
    def __init__(self, key, value):
        self.key = key;
        self.value = value;

'''
A common interface for replacement algos, which decide which item in a CacheSet to evict
'''

class IReplacementAlgo:
    # TODO: Define the interface for replacement algos...
    pass;

class LRUReplacementAlgo(IReplacementAlgo):
    Name = "LRUReplacementAlgo";
    # TODO: Implement the interface defined above

class MRUReplacementAlgo(IReplacementAlgo):
    Name = "MRUReplacementAlgo";
    # TODO: Implement the interface defined above


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
        # algo = ReplacementAlgoFactory.createReplacementAlgo("MRUReplacementAlgo");

        return SetAssociativeCache(setCount, setSize);

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
    def createReplacementAlgo(replacementAlgoName):
        if replacementAlgoName == LRUReplacementAlgo.Name:
            return LRUReplacementAlgo();
        elif replacementAlgoName == MRUReplacementAlgo.Name:
            return MRUReplacementAlgo();
        else:
            raise FormatError("Unknown replacement algo '%s'" % replacementAlgoName);

# ^^ ######################### END Helper Classes ######################### ^^
# ^^ ######################### BEGIN FOOTER ############################### ^^

if __name__ == "__main__":
    file = open('input009.txt')
    run = SetAssociativeCacheRunner()
    run.parseInput(file)