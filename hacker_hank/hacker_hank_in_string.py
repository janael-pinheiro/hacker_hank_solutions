def hacker_hank_in_string(s: str):
    response = "NO"
    desired = "hackerrank"
    desired_length = len(desired)
    input_length = len(s)
    i, j = 0, 0
    found_indexes = []
    while i < desired_length and j < input_length:
        if desired[i] == s[j]:
            found_indexes.append(j)
            i += 1
        j += 1
    if len(found_indexes) == desired_length:
        response = "YES"
    return response
