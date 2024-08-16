def chocolate_feast(n, c, m) -> int:
    bought = n // c
    total = bought
    if bought % m != 0:
        total += bought // m
        total += ((bought // m) + (bought % m)) // m
    else:
        remain = bought
        while remain // m > 0:
            total += (remain // m)
            remain = (remain // m) + (remain % m)
    return total
