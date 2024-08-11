def game_of_thrones(s: str):
    counter = {}
    for character in s:
        count = counter.get(character, 0)
        counter[character] = count + 1
    response = "YES"
    if len(s) % 2 == 0:
        for count in counter.values():
            if count % 2 != 0:
                return "NO"
    else:
        odd_count = 0
        for count in counter.values():
            if count % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return "NO"
    return response
