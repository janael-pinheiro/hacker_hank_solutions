from typing import List, Union


def minimum_bribes(q: List[int]):
    number_bribes = 0
    index = 0
    while index < len(q) - 1:
        if q[index] > q[index+1]:
            current = q[index]
            bribes = 0
            temp_index = index
            while (temp_index < len(q) - 1 and current > q[temp_index+1]) and bribes <= 2:
                temp = q[temp_index]
                q[temp_index] = q[temp_index+1]
                q[temp_index+1] = temp
                bribes += 1
                temp_index += 1
                number_bribes += 1
            if bribes > 2:
                print("Too chaotic")
                return
            if index > 0:
                index -= 1
        else:
            index += 1
    print(number_bribes)
    # index = 1
    # bribes_per_person = {}
    # while index < len(q):
    #     if q[index] < q[index-1]:
    #         current = q[index]
    #         bribes = bribes_per_person.get(current, 0)
    #         while (index > 0 and current < q[index-1]) and bribes <= 2:
    #             other_person_bribes = bribes_per_person.get(q[index - 1], 0)
    #             bribes_per_person[q[index - 1]] = other_person_bribes + 1
    #             bribes += 1
    #             bribes_per_person[current] = bribes
    #             temp = q[index]
    #             q[index] = q[index-1]
    #             q[index-1] = temp
    #             number_bribes += 1
    #             index -= 1
    #         if max(bribes_per_person.values()) > 2:
    #             print("Too chaotic")
    #             return
    #     index += 1
