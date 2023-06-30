def solve_maze(maze):
    if maze_solver(maze, 0, 0):
        print("Path found:")
        print_maze(maze)
    else:
        print("No path exists.")

def maze_solver(maze, row, col):
    if row == len(maze) - 1 and col == len(maze[0]) - 1 and maze[row][col] == 1:
        maze[row][col] = 2
        return True

    if is_safe(maze, row, col):
        maze[row][col] = 2

        if maze_solver(maze, row + 1, col):
            return True

        if maze_solver(maze, row, col + 1):
            return True

        maze[row][col] = 0
        return False

    return False

def is_safe(maze, row, col):
    rows = len(maze)
    cols = len(maze[0])

    if row >= 0 and row < rows and col >= 0 and col < cols and maze[row][col] == 1:
        return True

    return False

def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end=" ")
        print()

# Example maze (1 represents open path, 0 represents blocked path)
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
