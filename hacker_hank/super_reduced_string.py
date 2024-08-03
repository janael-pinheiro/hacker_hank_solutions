def super_reduced_string(s: str):
    response = "Empty String"
    stack = []
    stack.insert(0, s[0])
    current_index = 1
    while current_index < len(s):
        if len(stack) == 0:
            stack.insert(0, s[current_index])
            current_index += 1
            continue
        letter = stack.pop(0)
        if letter != s[current_index]:
            stack.insert(0, letter)
            stack.insert(0, s[current_index])
        current_index += 1
    if len(stack) > 0:
        response = "".join(stack[::-1])
    return response
