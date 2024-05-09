from collections import deque

def escape_possible(n, m, area):
    dx = [ 1, 0]
    dy = [0,  1]

    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return 1
        
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or area[nx][ny] == 0:
                continue
            
            area[nx][ny] = 0
            queue.append((nx, ny))
    
    return 0

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

result = escape_possible(n, m, area)
print(result)