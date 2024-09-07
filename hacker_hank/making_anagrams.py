def making_anagrams(s1: str, s2: str):
    number_deletions = 0
    s1_count = {}
    s2_count = {}
    unique_letters = set(s1+s2)
    for letter in unique_letters:
        s1_count[letter] = s1.count(letter)
        s2_count[letter] = s2.count(letter)
    for letter in unique_letters:
        number_deletions += abs(s1_count[letter] - s2_count[letter])
    return number_deletions
