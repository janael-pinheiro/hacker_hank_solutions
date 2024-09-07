from typing import Tuple


def bubble_sort(a) -> Tuple[int, int, int]:
    swaps_count = 0
    i = 0
    while i < len(a):
        j = 0
        while j < len(a) - 1:
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swaps_count += 1
            j += 1
        i += 1
    return swaps_count, a[0], a[-1]


def count_swaps(a):
    swaps_count, first_element, last_element = bubble_sort(a)
    print(f"Array is sorted in {swaps_count} swaps.")
    print(f"First Element: {first_element}")
    print(f"Last Element: {last_element}")
