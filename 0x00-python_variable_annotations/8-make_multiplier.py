#!/usr/bin/env python3
"""function that takes a list of floats as args"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that takes a float and returns a function"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
