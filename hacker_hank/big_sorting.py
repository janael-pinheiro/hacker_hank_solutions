from typing import List


def is_lower(first_number: str, second_number: str) -> bool:
    number_digits = 1
    response = False
    stop = False
    while not stop and number_digits <= len(first_number):
        if int(first_number[0:number_digits]) < int(second_number[0:number_digits]):
            response = True
            stop = True
        number_digits += 1
    return response


def merge_two_arrays(left_array: List[str], right_array: List[str]) -> List[str]:
    sorted_array: List[str] = []
    i, j = 0, 0

    while i < len(left_array) and j < len(right_array):
        if len(left_array[i]) < len(right_array[j]):
            sorted_array.append(left_array[i])
            i += 1
        elif len(left_array[i]) == len(right_array[j]):
            if is_lower(left_array[i], right_array[j]):
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                j += 1
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


def sort(values: List[str], left: int, right: int) -> List[str]:
    if left == right:
        return [values[left]]

    middle = (left + right) // 2
    left_array = sort(values, left, middle)
    right_array = sort(values, middle + 1, right)
    return merge_two_arrays(left_array, right_array)


def big_sorting(unsorted: List[str]):
    sorted_values = list(unsorted)
    return sort(sorted_values, 0, len(sorted_values)-1)

