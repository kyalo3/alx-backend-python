#!/usr/bin/env python3
"""function that takes a list of floats as args"""
from typing import List, Union


def to_kv(k: str, v:[Union[int, float]]) -> tuple[str, float]:
    """returns tuple"""
    return (k, v ** 2)
