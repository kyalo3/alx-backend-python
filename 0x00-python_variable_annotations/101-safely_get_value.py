#!/usr/bin/env python3
"""function add type annotations"""
from typing import Callable, Iterator, Union, Sequence, Any, TypeVar, Mapping
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """return values"""
    if key in dct:
        return dct[key]
    else:
        return default
