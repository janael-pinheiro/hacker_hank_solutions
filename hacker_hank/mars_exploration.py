def mars_exploration(s):
    number_errors = 0
    for index in range(0, len(s)-2, 3):
        if s[index] != "S":
            number_errors += 1
        if s[index+1] != "O":
            number_errors += 1
        if s[index+2] != "S":
            number_errors += 1
    return number_errors
