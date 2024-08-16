from typing import List


def gem_stones(arr: List[str]):
    count = 0
    base_elements = set(arr[0])
    for element in base_elements:
        s = 1
        for stone in arr[1:]:
            if element in stone:
                s += 1
        if s == len(arr):
            count += 1
    return count
