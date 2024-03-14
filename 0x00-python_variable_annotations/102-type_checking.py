#!/usr/bin/env python3
from typing import List, Tuple
"""function"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
