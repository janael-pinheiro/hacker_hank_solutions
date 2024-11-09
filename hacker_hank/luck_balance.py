from typing import List


def luck_balance(k: int, contests: List[List[int]]):
    important = list(filter(lambda x: x[1] == 1, contests))
    sorted_important = sorted(important, reverse=True, key=lambda x: x[0])
    not_important = list(filter(lambda x: x[1] == 0, contests))
    not_important_sum = 0
    for x in not_important:
        not_important_sum += x[0]
    important_sum = 0
    for index, value in enumerate(sorted_important):
        if index < k:
            important_sum += value[0]
        else:
            important_sum -= value[0]
    return important_sum + not_important_sum
