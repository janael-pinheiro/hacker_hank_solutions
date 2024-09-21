def get_max(operations):
    stack = []
    maximum_elements_stack = []
    current_max = 0
    response = []
    for operation in operations:
        input_operation = operation.split(" ")
        if input_operation[0] == "1":
            value = int(input_operation[1])
            if value >= current_max:
                if current_max != 0:
                    maximum_elements_stack.insert(0, current_max)
                    current_max = value
                else:
                    current_max = value
            stack.insert(0, value)
        elif input_operation[0] == "2":
            current = stack.pop(0)
            if current == current_max:
                if len(maximum_elements_stack) > 0:
                    current_max = maximum_elements_stack.pop(0)
                else:
                    current_max = 0
        elif input_operation[0] == "3":
            response.append(current_max)
    return response
