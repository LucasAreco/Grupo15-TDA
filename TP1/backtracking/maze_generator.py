from random import randint


def generate_maze(n, m):
    maze = [["X"] * m for _ in range(n)]
    
    for r in range(1, n-1):
        for c in range(1, m-1):
            p = randint(0, 100)
            if p < 80:
                maze[r][c] = "0"
            else:
                maze[r][c] = "X"

    maze[1][0] = "E"
    # liberamos la entrada:
    maze[1][1] = "0"
    maze[1][2] = "0"

    maze[n-1][m-2] = "S"
    # liberamos la salida:
    maze[n-2][m-1] = "0"
    maze[n-2][m-2] = "0"
    return maze

def generate_mazes_avg():
    dims = [(50, 50), (100, 100), (200, 200), (300, 300), (400, 400), (500, 500), (600, 600), (700, 700), (800, 800), (900, 900), (1000, 1000), (1100, 1100), (1200, 1200), (1300, 1300), (1400, 1400), (1500, 1500)]
    for n, m in dims:
        for i in range(3):
            maze = generate_maze(n, m)
            with open(f"data/input/maze_{n}x{m}_{i}.csv", "w") as file:
                for row in maze:
                    file.write(",".join(row) + "\n") 

def generate_worst_case(n, m):
    maze = [["X" for _ in range(m)] for _ in range(n)]
    for r in range(1, n-1):
        if r % 2 != 0: 
            for c in range(1, m-1): maze[r][c] = "0"

        if r % 4 == 1: maze[r+1][m-2] = "0"
        if r % 4 == 3: maze[r+1][1] = "0"
    
    maze[1][1] = "E"

    last_row = n-2 if (n-2)%2 != 0 else n-3
    maze[last_row][1 if (last_row//2)%2 != 0 else m-2] = "S"
    return maze

def generate_worst_cases():
    dims = []
    for i in range(50, 2000, 250):
        for j in range(50, 2000, 250):
            dims.append((i, j))
    print(dims)
    for n, m in dims:
        maze = generate_worst_case(n, m)
        with open(f"data/input/worst_case/maze_{n}x{m}.csv", "w") as file:
            for row in maze:
                file.write(",".join(row) + "\n") 

maze = generate_maze(10, 15)
with open(f"data/input/basic_case/maze_10x15.csv", "w") as file:
    for row in maze:
        file.write(",".join(row) + "\n") 