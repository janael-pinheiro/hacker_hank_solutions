def count_special_problems(
        lower: int,
        upper: int,
        problems: int,
        next_page: int,
        k: int) -> int:
    special_problems = 0
    while upper <= problems:
        if next_page >= lower and next_page <= upper:
            special_problems += 1
        if upper == problems:
            break
        next_page += 1
        lower = upper + 1
        upper = min(problems, upper + k)
    return special_problems


def count(current_page: int, problems: int, k: int):
    special_problems = 0
    page = current_page
    factor = 1
    lower = 1
    if k == 1 and current_page == 1:
        return problems

    while lower < page:
        upper = min(factor * k, problems)
        if lower <= page <= upper:
            special_problems += 1
        if upper == problems:
            break
        page += 1
        factor += 1
        lower = upper + 1
    if lower == page:
        special_problems += 1
    return special_problems


def workbook(n, k, arr):
    number_special_problems = 0
    current_page = 1

    for problems in arr:
        number_special_problems += count(current_page, problems, k)
        if problems % k == 0:
            current_page += problems // k
        else:
            current_page += (problems // k) + 1
    return number_special_problems
