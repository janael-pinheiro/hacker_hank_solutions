def counting_sort_1(arr):
    frequencies = [0] * 100
    for value in arr:
        current_frequency = frequencies[value]
        frequencies[value] = current_frequency + 1
    return frequencies
