#!/usr/bin/env python3
"""
0-simple_helper_function.py
This module provides a simple helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page  and page_size.

    Parameters:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - Tuple[int, int]: A tuple containing the start index and the end index.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
