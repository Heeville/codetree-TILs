def count_cells(grid, n):
    count = 0


    for i in range(n):
        for j in range(n):
            neighbor_count = 0
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    neighbor_count += 1
            
            if neighbor_count >= 3:
                count += 1

    return count

n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(count_cells(grid, n))