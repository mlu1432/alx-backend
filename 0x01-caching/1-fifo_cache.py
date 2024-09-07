#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a FIFO caching system.
    
    When the number of items exceeds the MAX_ITEMS limit, the first added
    item (FIFO) is discarded.
    """

    def __init__(self):
        """ Initialize the class with a deque to track the order of keys """
        super().__init__()
        self.queue = deque()  # Use deque to maintain insertion order

    def put(self, key, item):
        """
        Add an item to the cache using the FIFO policy.
        
        Args:
            key: The key to store the item.
            item: The value to store in the cache.
        """
        if key is None or item is None:
            return
        
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.popleft()
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

        self.cache_data[key] = item
        if key not in self.queue:
            self.queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        
        Args:
            key: The key to retrieve the value for.
        
        Returns:
            The value associated with the key, None if the key does not exist.
        """
        return self.cache_data.get(key, None)
