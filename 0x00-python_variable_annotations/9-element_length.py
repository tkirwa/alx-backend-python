#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in an iterable and return a list
    of tuples, where each tuple contains the original element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        a sequence from 'lst' and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
