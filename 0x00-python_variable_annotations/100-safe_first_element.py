#!/usr/bin/env python3

from typing import Any, List, Sequence, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
