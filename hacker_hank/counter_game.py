def is_power_of_two(number: int) -> bool:
    return number & (number - 1) == 0


def get_nearest_power_of_two(number: int) -> int:
    number_bit_length = number.bit_length()
    return 2 ** (number_bit_length - 1)


def counter_game(n):
    response = "Richard"
    if n == 1:
        return response
    current = n
    queue = ["Louise", "Richard"]
    while current > 1:
        response = queue.pop(0)
        if is_power_of_two(current):
            current = current // 2
        else:
            nearest_power_of_two = get_nearest_power_of_two(current)
            current -= nearest_power_of_two
        queue.append(response)
    return response
