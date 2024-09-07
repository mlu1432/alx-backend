#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache implements a Least Frequently Used (LFU) caching system.

    When the number of items exceeds the MAX_ITEMS limit, the least frequently
    used item is discarded. If multiple items have the same frequency,the Least
    Recently Used (LRU) item is discarded.
    """

    def __init__(self):
        """ Initialize the class with frequency and usage tracking """
        super().__init__()
        self.freq = defaultdict(int)  # Track frequency of each key
        self.usage_order = []  # Track order of usage for LRU tie-breaking

    def put(self, key, item):
        """
        Add an item to the cache using the LFU policy.

        Args:
            key: The key to store the item.
            item: The value to store in the cache.
        """
        if key is None or item is None:
            return

        # If key exists, update the item and move it to the front of the usage list
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)  # Mark as most recently used
        else:
            # If cache exceeds MAX_ITEMS, discard the least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the key with the least frequency
                least_freq = min(self.freq.values())
                least_used = [k for k in self.usage_order if self.freq[k] == least_freq]

                # Discard the least recently used item from the least frequently used items
                key_to_discard = least_used[0]
                print("DISCARD:", key_to_discard)
                del self.cache_data[key_to_discard]
                del self.freq[key_to_discard]
                self.usage_order.remove(key_to_discard)

            # Add the new item
            self.cache_data[key] = item
            self.freq[key] = 1  # Initialize frequency
            self.usage_order.append(key)  # Mark as most recently used

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,or None if the key does not exist
        """
        if key in self.cache_data:
            self.freq[key] += 1  # Increase frequency count
            self.usage_order.remove(key)
            self.usage_order.append(key)  # Mark as most recently used
            return self.cache_data[key]
        return None
