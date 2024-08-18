def quick_sort_1_partition(arr):
    pivot = arr[0]
    left = []
    right = []
    equal = []
    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            equal.append(value)
    response = []
    response.extend(left)
    response.extend(equal)
    response.extend(right)
    return response
