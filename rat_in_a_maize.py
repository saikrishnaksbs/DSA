def free_rat(i,j , maze, route):
    if i == 3 and j == 3:
        print(route)
        exit()
    if i > 3 or i < 0 or j < 0 or j > 3:
        return 
    if maze[i][j]==1:
        route.append([i,j])
    else:
        return

    free_rat(i+1,j,maze,route)
    free_rat(i,j+1,maze,route)
    free_rat(i-1,j,maze,route)
    free_rat(i,j-1,maze,route)


maze = [
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]
free_rat(0,0,maze, [])