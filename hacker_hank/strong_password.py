import string


def minimum_number(n: int, password: str):
    minimum_password_length = 6
    has_number = 1
    has_lower_case = 1
    has_upper_case = 1
    has_special_character = 1
    desired = 0
    for character in set(password):
        if has_number + has_lower_case + has_upper_case + has_special_character == desired:
            break
        if character in string.digits:
            has_number = 0
        elif character in string.ascii_lowercase:
            has_lower_case = 0
        elif character in string.ascii_uppercase:
            has_upper_case = 0
        elif character in "!@#$%^&*()-+":
            has_special_character = 0
    total_required = has_number + has_lower_case + has_upper_case + has_special_character
    return max(total_required, minimum_password_length - n)
