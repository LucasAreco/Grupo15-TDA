"""
Suposiciones: el problema comienza siempre desde una posición conocida y con una dirección conocida.

Las posiciones se indican en el formato (fila, columna, direccion)


"""

def get_next_pos(maze, position):
    row, col, direc = position
    next_pos = None
    if direc == "N" and row - 1 >= 0:
        next_pos = (row - 1, col, direc)
    elif direc == "S" and row + 1 < len(maze):
        next_pos = (row + 1, col, direc)
    elif direc == "W" and col - 1 >= 0:
        next_pos = (row, col - 1, direc)
    elif direc == "E" and col + 1 <= len(maze[0]):
        next_pos = (row, col + 1, direc)
    
    if next_pos:
        if maze[next_pos[0]][next_pos[1]] != "X":
            return next_pos
    return None

def turn_left(position):
    row, col, direc = position
    new_direc = direc
    if direc == "N":
        new_direc = "W"
    elif direc == "S":
        new_direc = "E"
    elif direc == "W":
        new_direc = "S"
    else:
        new_direc = "N"

    return (row, col, new_direc)
    
def find_next_step(maze, pos, paths, visited):
    row, col, _ = pos
    if pos in visited: return None
    if maze[row][col] == "S": return paths
    
    visited.add(pos)

    sol = None
    next_pos = get_next_pos(maze, pos)
    if next_pos:
        print(f"Avanzo desde {pos} a {next_pos}")
        paths[(next_pos[0], next_pos[1])] = (pos[0], pos[1])  
        sol = find_next_step(maze, next_pos, paths, visited)
    
    if not sol:
        next_pos = turn_left(pos)
        print(f"Giro desde {pos} a {next_pos}")
        sol = find_next_step(maze, next_pos, paths, visited)
    
    return sol

def find_path(maze, entry): 
    paths = {}
    visited = set()

    return find_next_step(maze, entry, paths, visited)

maze = [
    ['X', 'X', 'X', 'X'], 
    ['X', 'X', 'O', 'S'], 
    ['X', 'O', 'O', 'X'], 
    ['X', 'E', 'X', 'X']
    ]

print(find_path(maze, (3, 1, "N")))