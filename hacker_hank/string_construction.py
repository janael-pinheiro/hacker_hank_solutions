def string_construction(s: str):
    found_letters = {}
    cost = 0
    for letter in s:
        if letter not in found_letters:
            cost += 1
            found_letters[letter] = True
    return cost
