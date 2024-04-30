directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # N, W, S, E
x, y = 0, 0
idx=0

commands=input()

for command in commands:
    if command == 'L':
        idx = (idx + 1) % 4 
    elif command == 'R':
        idx = (idx - 1) % 4  
    elif command == 'F':
        dx, dy = directions[idx]  
        x += dx
        y += dy


print(x, y)