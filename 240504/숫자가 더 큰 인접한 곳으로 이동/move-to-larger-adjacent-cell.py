def move(grid, r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    n = len(grid)
    result = []
    while True:
        result.append(grid[r][c]) 
        max_value = grid[r][c]   
        next_r, next_c = None, None
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > grid[r][c] and grid[nr][nc] > max_value:
                next_r, next_c = nr, nc
                max_value = grid[nr][nc]
                break

        if next_r is None or next_c is None:
            break
        r, c = next_r, next_c  
    return result

n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 이동 함수 호출하여 결과 출력
result = move(grid, r - 1, c - 1)
print(' '.join(map(str, result)))