def fill_snail_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0 

    row, col = 0, 0
    
    for i in range(1, n * m + 1):
        matrix[row][col] = i
        next_row = row + directions[dir_index][0]
        next_col = col + directions[dir_index][1]
        
        if (0 <= next_row < n and 0 <= next_col < m and matrix[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            dir_index = (dir_index + 1) % 4
            row += directions[dir_index][0]
            col += directions[dir_index][1]

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


n, m = map(int, input().split())

resulting_matrix = fill_snail_matrix(n, m)

print_matrix(resulting_matrix)