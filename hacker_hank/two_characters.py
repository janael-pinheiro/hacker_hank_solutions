from typing import Dict, Tuple, List


def create_characters_counter(s: str) -> Dict[str, Tuple[int, List]]:
    counter = {}
    for index, character in enumerate(s):
        c = counter.get(character, (0, []))
        new_count = c[0] + 1
        new_list = c[1] + [index]
        counter[character] = (new_count, new_list)
    return counter


def is_alternating_characters(first: List[int], second: List[int]) -> bool:
    minimum_length = min(len(first), len(second))
    count = 0
    valid_count_1 = 0
    valid_count_2 = 0
    while count < len(first) and count < len(second):
        valid_count_1 += int(first[count] > second[count])
        valid_count_2 += int(first[count] < second[count])
        count += 1
    return valid_count_1 == minimum_length or valid_count_2 == minimum_length


def alternate(s: str) -> int:
    counter = create_characters_counter(s)
    sorted_count = sorted(counter.values(), key=lambda item: item[0], reverse=True)
    found = False
    index = 0
    number_alternating_characters = 0
    while not found and index < len(sorted_count) - 1:
        first_item = sorted_count[index]
        second_item = sorted_count[index+1]
        difference = abs(first_item[0] - second_item[0])
        if difference <= 1:
            is_alternating = is_alternating_characters(first_item[1], second_item[1])
            if is_alternating:
                number_alternating_characters = first_item[0] + second_item[0]
                found = True
        index += 1
    return number_alternating_characters
