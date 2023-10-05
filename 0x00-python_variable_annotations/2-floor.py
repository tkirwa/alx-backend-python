#!/usr/bin/env python3
"""Type-annotated function floor"""


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number as an integer.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The floor of the input number as an integer.
    """
    # Convert the float to an integer to get the floor value
    result = int(n)
    return result
