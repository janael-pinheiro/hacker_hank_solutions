from typing import List


def rot_left(a: List[int], d: int) -> List[int]:
    array_length = len(a)
    rotated_array = [0 for _ in range(array_length)]
    for index, value in enumerate(a):
        rotated_index = (index - d) % array_length
        rotated_array[rotated_index] = value
    return rotated_array
