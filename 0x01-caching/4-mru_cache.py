#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache implements a Most Recently Used (MRU) caching system.
    
    When the number of items exceeds the MAX_ITEMS limit, the most recently
    used item is discarded.
    """

    def __init__(self):
        """ Initialize the class with a tracker for most recently used key """
        super().__init__()
        self.mru_key = None  # Track the most recently used key

    def put(self, key, item):
        """
        Add an item to the cache using the MRU policy.
        
        Args:
            key: The key to store the item.
            item: The value to store in the cache.
        """
        if key is None or item is None:
            return

        # If the key exists, update the item and track it as most recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            self.mru_key = key
            return

        # If cache exceeds MAX_ITEMS, discard the most recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.mru_key is not None:
                print("DISCARD:", self.mru_key)
                del self.cache_data[self.mru_key]

        # Add the new item and update the most recently used key
        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        
        Args:
            key: The key to retrieve the value for.
        
        Returns:
            The value associated with the key, None if the key does not exist.
        """
        if key in self.cache_data:
            self.mru_key = key  # Mark the accessed item as most recently used
            return self.cache_data[key]
        return None
