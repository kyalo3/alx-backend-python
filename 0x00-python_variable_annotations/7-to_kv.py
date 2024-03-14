#!/usr/bin/env python3
"""function that takes a list of floats as args"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple"""
    return (k, v ** 2)
