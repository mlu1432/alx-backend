#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache implements a LIFO caching system.
    
    When the number of items exceeds the MAX_ITEMS limit, the last added
    item (LIFO) is discarded.
    """

    def __init__(self):
        """ Initialize the class with an empty last_key tracker """
        super().__init__()
        self.last_key = None  # Store the last added key

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO policy.
        
        Args:
            key: The key to store the item.
            item: The value to store in the cache.
        """
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                print("DISCARD:", self.last_key)
                del self.cache_data[self.last_key]
        
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        
        Args:
            key: The key to retrieve the value for.
        
        Returns:
            The value associated with the key,or None if the key does not exist
        """
        return self.cache_data.get(key, None)
