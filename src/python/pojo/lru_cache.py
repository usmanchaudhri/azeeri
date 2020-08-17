"""
LRU Cache - least recently used cache

An LRU cache is a system to store data in memory where the data eviction happens in a way where the least recently
used data is evicted or deleted from the cache. This ensures that the Cache is always filled with the required
data only. We would also need to ensure that the data used is marked as most recently used. Ensure the cache is
thread safe.

- insert key-value pairs
- retrieving a key-value pair
- retrieving the most recently used key with the
    getMostRecentKey()
-
"""
from collections import OrderedDict

class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get_from_cache(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def insert_into_cache(self, key, value):
        self.cache[key] = value

        # the items at the end of the list are the most recently used
        self.cache.move_to_end(key)
        if len(self.cache) >= self.capacity:
            # remove the least recently used item
            self.cache.popitem(last=False)

