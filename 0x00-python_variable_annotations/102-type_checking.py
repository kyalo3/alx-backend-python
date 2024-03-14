#!/usr/bin/env python3
"""function"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """return value"""
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
