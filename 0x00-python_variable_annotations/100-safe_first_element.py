#!/usr/bin/env python3
"""Defines a function to safely retrieve the first element of a sequence"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    :param lst: The input sequence.
    :return: The first element of the sequence or None if the
    sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
