def max_coins(grid):
    n = len(grid)
    max_coins_count = 0

    for i in range(n - 2):
        for j in range(n - 2):
            coins_count = 0
            for k in range(3):
                for l in range(3):
                    if grid[i + k][j + l] == 1:
                        coins_count += 1
            max_coins_count = max(max_coins_count, coins_count)

    return max_coins_count

n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(max_coins(grid))