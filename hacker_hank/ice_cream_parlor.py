from typing import List


def ice_cream_parlor(m: int, arr: List[int]):
    response = []
    for i in range(len(arr)-1):
        diff = m - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == diff:
                response = [i+1, j+1]
    return response
