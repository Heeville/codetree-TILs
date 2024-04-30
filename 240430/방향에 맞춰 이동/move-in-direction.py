dx = [1, -1, 0, 0]  
dy = [0, 0, -1, 1]  

N = int(input())
move = []
for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    move.append((direction, distance))

x, y = 0, 0
for i in range(N):
    direction, distance = move[i]
    if direction == 'E':
        index = 0
    elif direction == 'W':
        index = 1
    elif direction == 'S':
        index = 2
    elif direction == 'N':
        index = 3
    x += dx[index] * distance
    y += dy[index] * distance

print(x, y)