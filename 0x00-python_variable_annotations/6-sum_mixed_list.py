#!/usr/bin/env python3
"""function that takes a list of floats as args"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns their sum as a float"""
    return float(sum(mxd_list))
