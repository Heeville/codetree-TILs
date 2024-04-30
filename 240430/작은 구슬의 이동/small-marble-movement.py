def find_marble_position(n, t, r, c, d):
    direction_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    
    direction = direction_map[d]
    
    current_row, current_col = r, c
    
    current_time = 0
    
    while current_time < t:
        next_row = current_row + direction[0]
        next_col = current_col + direction[1]
        
        if next_row < 1 or next_row > n or next_col < 1 or next_col > n:
            direction = (-direction[0], -direction[1])
        else:
            current_row, current_col = next_row, next_col
        
        current_time += 1
    
    return current_row, current_col

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

final_row, final_col = find_marble_position(n, t, r, c, d)
print(final_row, final_col)