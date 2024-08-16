def beautiful_binary_string(b: str):
    undesired_string = "010"
    substring_hash = hash(undesired_string)
    count = 0
    i = 0
    while i <= len(b)-len(undesired_string):
        if hash(b[i:i+len(undesired_string)]) == substring_hash:
            count += 1
            i += 2
        i += 1
    return count

