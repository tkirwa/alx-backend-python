#!/usr/bin/env python3
"""Type-annotated function concat"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result as a string.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    # Concatenate the two input strings
    result = str1 + str2
    return result
