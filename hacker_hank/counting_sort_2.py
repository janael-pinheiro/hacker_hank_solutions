def counting_sort_2(arr):
    frequencies = [0] * 100
    for value in arr:
        current_frequency = frequencies[value]
        frequencies[value] = current_frequency + 1
    sorted_values = []
    for index, frequency in enumerate(frequencies):
        if frequency != 0:
            sorted_values.extend([index] * frequency)
    return sorted_values
