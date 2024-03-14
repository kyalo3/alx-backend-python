from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # Define array as a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Pass an integer factor

print(zoom_2x)
print(zoom_3x)
