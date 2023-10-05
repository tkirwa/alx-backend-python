#!/usr/bin/env python3
"""Type-annotated function to_str"""


def to_str(n: float) -> str:
    """
    Returns the string representation of a floating-point number.

    Args:
        n (float): The input floating-point number.

    Returns:
        str: The string representation of the input number.
    """
    # Convert the float to a string using the str() function
    result = str(n)
    return result
