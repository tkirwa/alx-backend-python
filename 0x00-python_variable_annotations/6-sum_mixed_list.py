#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
          and floats.

    Returns:
        float: The sum of the numbers in the input list as a float.
    """
    # Initialize a variable 'a' to store the sum
    a: float = 0.0

    # Iterate through the mixed list and add each element to 'a'
    for x in mxd_lst:
        a += x

    # Return the sum as a float
    return a
