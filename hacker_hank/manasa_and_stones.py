def stones(n, a, b):
    lower = 0
    upper = n - 1
    output = set()
    while upper >= 0:
        result = (lower * a) + (upper * b)
        output.add(result)
        lower += 1
        upper -= 1
    return sorted(list(output))
