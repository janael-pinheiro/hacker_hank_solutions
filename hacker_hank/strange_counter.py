from typing import Tuple


def get_initial_parameters(t: int) -> Tuple[int, int]:
    upper_limit = 3
    current_limit = 3
    initial_value = 3
    initial_t = 1
    while t > upper_limit:
        initial_t = upper_limit + 1
        current_limit *= 2
        upper_limit = upper_limit + current_limit
        initial_value *= 2
    return initial_t, initial_value


def find_value(temp_t, t, result_value):
    difference_t = t - temp_t
    return result_value - difference_t


def strange_counter(t):
    temp_t, initial_value = get_initial_parameters(t)
    result_value = find_value(temp_t, t, initial_value)
    return result_value
