def free_rat(i, j, maze, route):
    # Base case: destination is reached
    if i == 3 and j == 3:
        route.append([i, j])
        print("Path:", route)
        return True

    # Boundaries and obstacle check
    if i > 3 or i < 0 or j < 0 or j > 3 or maze[i][j] == 0:
        return False

    # Mark the current cell as visited by setting it to 0
    maze[i][j] = 0
    route.append([i, j])

    # Explore in all four directions
    if (free_rat(i + 1, j, maze, route) or
        free_rat(i, j + 1, maze, route) or
        free_rat(i - 1, j, maze, route) or
        free_rat(i, j - 1, maze, route)):
        return True

    # Backtrack: unmark this cell by restoring its original value
    route.pop()
    maze[i][j] = 1
    return False

# Define the maze
maze = [
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]

# Call the function
free_rat(0, 0, maze, [])
