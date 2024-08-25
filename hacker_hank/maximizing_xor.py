from typing import List


def decimal_to_binary(value) -> List[int]:
    result = value
    response = []
    while result > 0:
        response.insert(0, result % 2)
        result = result // 2
    return response


def binary_to_decimal(value: str) -> int:
    return int(value, 2)


def pad_value(value: List[int]) -> List[int]:
    r = 10 - len(value)
    response = [0] * r
    return response + value


def xor(left, right) -> List[int]:
    count = 0
    response = [0] * len(left)
    while count < len(left):
        if left[count] != right[count]:
            response[count] = 1
        count += 1
    return response


def maximizing_xor(l: int, r: int):
    left = l
    right = l + 1
    current_max = 0
    while left < r:
        while right <= r:
            binary_left = pad_value(decimal_to_binary(left))
            binary_right = pad_value(decimal_to_binary(right))
            xor_value = xor(binary_left, binary_right)
            decimal_value = binary_to_decimal("".join([str(x) for x in xor_value]))
            if decimal_value > current_max:
                current_max = decimal_value
            right += 1
        left += 1
        right = left + 1

    return current_max

