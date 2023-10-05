#!/usr/bin/env python3
"""Zoom Array

This script defines a function `zoom_array` that takes a tuple and an
integer factor as input. It returns a list containing each element of the
input tuple repeated `factor` times.

Example:
    zoom_array((12, 72, 91)) returns [12, 12, 72, 72, 91, 91].

Args:
    lst (Tuple): The input tuple.
    factor (int): The factor by which elements should be repeated
      (default is 2).

Returns:
    List: A list containing elements of the input tuple repeated according
      to the factor.

"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Repeats elements of a tuple in a list based on a factor."""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
