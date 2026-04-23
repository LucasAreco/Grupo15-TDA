def get_next_pos(maze, position):
    row, col, direc = position
    row_mov, col_mov = 0, 0    

    if direc  == "N":
        row_mov -= 1
    elif direc == "S":
        row_mov += 1
    elif direc == "W":
        col_mov -= 1
    elif direc == "E":
        col_mov += 1

    next_row = row + row_mov
    next_col = col + col_mov

    if (next_row >= 0 and next_row < len(maze)) and (next_col >= 0 and next_col < len(maze[0])):
        if maze[next_row][next_col] != "X":
            return (next_row, next_col, direc)

    return None

def turn_left(position):
    row, col, direc = position

    if direc == "N": return (row, col, "W")
    elif direc == "W": return (row, col, "S")
    elif direc == "S": return (row, col, "E")
    else: return (row, col, "N")
    
def find_next_step(maze, pos, visited):
    row, col, _ = pos
    if maze[row][col] == "S": return [pos]
    
    visited.add((row, col))

    sol = None
    next_pos = get_next_pos(maze, pos)
    if next_pos and (next_pos[0], next_pos[1]) not in visited:
        sol = find_next_step(maze, next_pos, visited)
        if sol:
            return [pos] + sol

    turn_left_pos = pos
    for _ in range(3): 
        turn_left_pos = turn_left(turn_left_pos)
        print(f"Giro a {turn_left_pos}")

        next_pos = get_next_pos(maze, turn_left_pos)
        if next_pos and (next_pos[0], next_pos[1]) not in visited:
            sol = find_next_step(maze, next_pos, visited)
            if sol:
                return [pos] + sol
    
    visited.remove((row, col))
    return sol

def find_path(maze, entry): 
    visited = set()

    return find_next_step(maze, entry, visited)
