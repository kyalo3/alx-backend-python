#!/usr/bin/env python3
"""function’s parameters and return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple, Any


def zoom_array(lst: Tuple, factor: int) -> List[Any]:

    return [x * factor for x in lst]
