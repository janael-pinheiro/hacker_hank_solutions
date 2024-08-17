def insertion_sort_1(n, arr):
    current_index = n - 1
    value = arr[current_index]
    keep_going = True
    while keep_going:
        if current_index > 0 and arr[current_index - 1] > value:
            arr[current_index] = arr[current_index - 1]
            print(" ".join([str(x) for x in arr]))
            current_index -= 1
        else:
            arr[current_index] = value
            print(" ".join([str(x) for x in arr]))
            keep_going = False
