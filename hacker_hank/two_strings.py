def two_strings(s1, s2):
    response = "NO"
    if len(s1) == 0 or len(s2) == 0:
        return response
    s1_unique_characters = set(s1)
    s2_unique_characters = set(s2)
    if len(s1_unique_characters) >= 26 or len(s2_unique_characters) >= 26:
        return "YES"

    for character in s1_unique_characters:
        if character in s2_unique_characters:
            response = "YES"
            break
    return response
