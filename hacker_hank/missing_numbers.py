from collections import Counter


def missing_numbers(arr, brr):
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    missing = []
    for number in brr:
        if number not in count_arr:
            missing.append(number)
        elif number in count_brr and count_arr[number] != count_brr[number]:
            missing.append(number)
    return sorted(set(missing))
