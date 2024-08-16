def must_replace(grid, current: int, line_number: int, column_number: int) -> bool:
    return (
            current > int(grid[line_number][column_number - 1])
            and current > int(grid[line_number][column_number + 1])
            and current > int(grid[line_number - 1][column_number])
            and current > int(grid[line_number + 1][column_number]))


def cavity_map(grid):
    grid_copy = list(grid)
    start_line = 1
    start_column = 1
    for line_number in range(start_line, len(grid)-1):
        s = [c for c in grid[line_number]]
        for column_number in range(start_column, len(grid[line_number])-1):
            current = int(grid[line_number][column_number])
            if current == 1:
                continue
            if must_replace(grid, current, line_number, column_number):
                s[column_number] = "X"
        grid_copy[line_number] = "".join(s)
    return grid_copy
