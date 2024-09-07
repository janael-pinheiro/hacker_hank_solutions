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


def maximum_toys(prices, k):
    sorted_prices = sort(prices, 0, len(prices) - 1)
    index = 0
    sum_prices = 0
    count = 0
    while sum_prices <= k and index < len(prices):
        sum_prices += sorted_prices[index]
        index += 1
        count += 1
    if sum_prices > k:
        count -= 1
    return count
