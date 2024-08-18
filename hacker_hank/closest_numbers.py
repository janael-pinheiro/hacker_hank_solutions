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


def closest_numbers(arr):
    sorted_arr = sort(arr, 0, len(arr)-1)
    closest = abs(sorted_arr[0] - sorted_arr[1])
    index = 2
    cache = {closest: [sorted_arr[0], sorted_arr[1]]}
    while index < len(sorted_arr):
        difference = abs(sorted_arr[index] - sorted_arr[index-1])
        c = cache.get(difference, [])
        c.append(sorted_arr[index-1])
        c.append(sorted_arr[index])
        cache[difference] = c
        if difference < closest:
            closest = difference
        index += 1
    return cache[closest]
