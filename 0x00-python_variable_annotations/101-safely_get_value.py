#!/usr/bin/env python3
"""Advanced type annotated function"""
from typing import Any, Mapping, TypeVar, Union

# Create a generic type variable T
T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary or returns a default value.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return if...
          the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or
        the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
