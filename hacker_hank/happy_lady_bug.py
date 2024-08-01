from typing import Dict, List


def compute_count(b: str):
    has_empty_space = False
    count_lady_bug = {}
    color_index = {}
    for index, letter in enumerate(b):
        if letter == "_":
            has_empty_space = True
            continue
        count = count_lady_bug.get(letter, 0)
        count_lady_bug[letter] = count + 1
        color = color_index.get(letter, [])
        color.append(index)
        color_index[letter] = color

    return count_lady_bug, color_index, has_empty_space


def check_already_happy_lady_bug(color_index: Dict[str, List[int]]):
    for value in color_index.values():
        for index in range(0, len(value) - 1):
            if value[index + 1] - value[index] != 1:
                return False
    return True


def happy_lady_bug(b):
    response = "NO"
    count_lady_bug, color_index, has_empty_space = compute_count(b)
    if not count_lady_bug and has_empty_space:
        return "YES"
    sorted_values = sorted(count_lady_bug.values())
    for value in sorted_values:
        if value == 1:
            return response
        else:
            break
    only_one_color = len(count_lady_bug.keys()) == 1
    if has_empty_space or not has_empty_space and only_one_color:
        return "YES"
    else:
        if check_already_happy_lady_bug(color_index):
            response = "YES"
    return response
