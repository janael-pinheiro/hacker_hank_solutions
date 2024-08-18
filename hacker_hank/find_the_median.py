from typing import List


def merge_two_arrays(left_array: List[int], right_array: List[int]) -> List[int]:
    sorted_array: List[int] = []
    i, j = 0, 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            j += 1

    if i == len(left_array):
        while j < len(right_array):
            sorted_array.append(right_array[j])
            j += 1

    if j == len(right_array):
        while i < len(left_array):
            sorted_array.append(left_array[i])
            i += 1

    return sorted_array


def sort(values: List[int], left: int, right: int) -> List[int]:
    if left == right:
        return [values[left]]

    middle = (left + right) // 2
    left_array = sort(values, left, middle)
    right_array = sort(values, middle + 1, right)
    return merge_two_arrays(left_array, right_array)


def find_the_median(arr):
    sorted_arr = sort(arr, 0, len(arr) - 1)
    middle = len(arr) // 2
    return sorted_arr[middle]
