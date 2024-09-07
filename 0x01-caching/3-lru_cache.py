#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache implements a Least Recently Used (LRU) caching system.

    When the number of items exceeds the MAX_ITEMS limit, the least recently
    used item is discarded.
    """

    def __init__(self):
        """ Initialize class with an OrderedDict to track order of usage """
        super().__init__()
        self.cache_data = OrderedDict()  # OrderedDict will help track LRU order

    def put(self, key, item):
        """
        Add an item to the cache using the LRU policy.

        Args:
            key: The key to store the item.
            item: The value to store in the cache.
        """
        if key is None or item is None:
            return

        # If the key exists, move it to the end (most recently used)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        # If cache exceeds MAX_ITEMS, discard the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", oldest_key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, None if the key does not exist.
        """
        if key in self.cache_data:
            # Move the accessed item to the end (most recently used)
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
