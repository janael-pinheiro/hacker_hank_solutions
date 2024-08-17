def insertion_sort_2(n, arr):
    i = 1
    while i < n:
        if arr[i] < arr[i-1]:
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                j -= 1
        print(" ".join([str(x) for x in arr]))
        i += 1
