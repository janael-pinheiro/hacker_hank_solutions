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
    r = 32 - len(value)
    response = [1] * r
    return response


def flip(value: List[int]) -> List[int]:
    return [int(not v) for v in value]


def flipping_bits(n):
    binary_value = decimal_to_binary(n)
    values_to_pad = pad_value(binary_value)
    flipped_value = flip(binary_value)
    combined = list(values_to_pad)
    combined.extend(flipped_value)
    return binary_to_decimal("".join([str(x) for x in combined]))
