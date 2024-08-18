def running_time_of_algorithms(arr):
    number_operations = 0
    n = len(arr)
    i = 1
    while i < n:
        if arr[i] < arr[i - 1]:
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                j -= 1
                number_operations += 1
        i += 1
    return number_operations
