def append_and_delete(s: str, t: str, k: int):
    response = "Yes"
    if len(s) + len(t) <= k:
        return response
    if s == t and k % 2 == 0:
        return response
    count = 0
    s_length = len(s)
    t_length = len(t)
    minimum = min(s_length, t_length)
    while count < minimum:
        if s[count] != t[count]:
            break
        count += 1
    needed_number_operations = (s_length - count) + (t_length - count)
    if needed_number_operations == k:
        return response
    elif needed_number_operations < k and k % 2 != 0:
        return response
    elif needed_number_operations < k and needed_number_operations == k * 0.5 and k > 2:
        return response
    return "No"

