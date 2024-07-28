def is_funny_string(input_string: str) -> str:
    current_forward = 0
    end = len(input_string) - 1
    current_backward = end

    for _ in range(end - 1):
        absolute_difference_forward = abs(ord(input_string[current_forward]) - ord((input_string[current_forward+1])))
        absolute_difference_backward = abs(ord(input_string[current_backward]) - ord(input_string[current_backward-1]))
        if absolute_difference_forward != absolute_difference_backward:
            return "Not Funny"
        current_forward += 1
        current_backward -= 1
    return "Funny"
