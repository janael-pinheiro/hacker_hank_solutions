from typing import List


def macs_cake_walk(calorie: List[int]):
    total = 0
    calories = list(calorie)
    sorted_calories = sorted(calories, reverse=True)
    for exponent, cal in enumerate(sorted_calories):
        total += (2 ** exponent) * cal
    return total
