
def grid_search(G, P) -> str:
    first_row_pattern_index = 0
    current_row_grid_index = 0
    current_column_grid_index = 0
    hashed_combined_pattern = hash("".join(P))
    hashed_first_pattern_row = hash(P[first_row_pattern_index])
    length_row_pattern = len(P[first_row_pattern_index])
    while current_row_grid_index + len(P) <= len(G):
        length_row_grid = len(G[current_row_grid_index])
        while current_column_grid_index + length_row_pattern <= length_row_grid:
            current = G[current_row_grid_index][current_column_grid_index:current_column_grid_index + len(P[first_row_pattern_index])]
            if hash(current) == hashed_first_pattern_row:
                combined_grid = current
                count = 1
                row_index = current_row_grid_index + 1
                while count < len(P):
                    combined_grid += G[row_index][current_column_grid_index:current_column_grid_index + len(P[count])]
                    count += 1
                    row_index += 1
                if hash(combined_grid) == hashed_combined_pattern:
                    return "YES"
            current_column_grid_index += 1
        current_column_grid_index = 0
        current_row_grid_index += 1
    return "NO"
