from typing import List


def fair_rations(b: List[int]):
    count = 0
    for index, _ in enumerate(b):
        if len(b) == 2 and ((b[index] % 2 != 0 and b[index+1] % 2 == 0) or (b[index] % 2 == 0 and b[index+1] % 2 != 0)):
            return 'NO'
        if b[index] % 2 == 0:
            continue
        b[index] += 1
        if index + 1 < len(b):
            b[index + 1] += 1
        else:
            return 'NO'
        count += 2

    return str(count)
