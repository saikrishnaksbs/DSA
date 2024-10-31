def nqueens(arr, row):
    
    if row == len(arr):
        print(arr)
        exit()
    
    place_the_queen(arr, row)

def place_the_queen(arr, row):
    for col in range(len(arr)):
        if is_valid(arr, row, col):
            arr[row][col] = 'Q'
            nqueens(arr, row + 1)
            arr[row][col] = '-'
    
def is_valid(arr, row, col):
    # check if it is safe to place the queen in the that row
    for i in range(len(arr[row])):
        if arr[row][i] == 'Q':
            return False
    
    # check if it is safe to place the queen in the that column
    for i in range(len(arr)):
        if arr[i][col] == 'Q':
            return False
    
    # check if it is safe to place the queen in the diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if arr[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while i < len(arr) and j >= 0:
        if arr[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    
    return True

nqueens([['-','-','-','-'], ['-','-','-','-'], ['-','-','-','-'], ['-','-','-','-']], 0)