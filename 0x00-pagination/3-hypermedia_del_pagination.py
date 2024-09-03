#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
        - List[List]: A list of lists where each list contains data from
          the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0

        Returns:
        - Dict[int, List]: A dictionary where the key is the index, and
          the value is the data.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination details for deletion-resilient
        hypermedia pagination.

        Parameters:
        - index (int): The start index of the page.
        - page_size (int): The number of items per page.

        Returns:
        - Dict[str, Any]: A dictionary containing the pagination details.
        """
        assert index is not None and 0 <= index < len(self.indexed_dataset()), \
            "Index out of range"

        data = []
        next_index = index
        count = 0

        while count < page_size and next_index < len(self.indexed_dataset()):
            if next_index in self.indexed_dataset():
                data.append(self.indexed_dataset()[next_index])
                count += 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
