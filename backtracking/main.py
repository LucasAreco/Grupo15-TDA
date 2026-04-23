from bt import find_path


def main(args: list[str]) -> None:
    input_file = args[0] if len(args) > 0 else "data/maze.csv"
    with open(input_file, "r") as file:
        maze =  [line.strip().split(",") for line in file]
    start_pos = find_entry(maze)
    if not start_pos:
        print("No se encontró la entrada en el laberinto.")
        return
    path = find_path(maze, start_pos)
    print("Laberinto:")
    for row in maze:
        print(" ".join(row))
    
    print(f"Camino encontrado: {path}")


def find_entry(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "E":
                return (i, j, "N")  
    return None

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])