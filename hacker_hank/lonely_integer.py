def lonely_integer(a):
    count = {}
    response = 0
    for integer in a:
        c = count.get(integer, 0)
        count[integer] = c + 1
    for key, value in count.items():
        if value == 1:
            response = key
            break
    return response
