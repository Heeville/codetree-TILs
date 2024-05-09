def escape_possible(n, m, area):
    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return True
        
        if x + 1 < n and area[x + 1][y] == 1 and dfs(x + 1, y):
            return 1
        if y + 1 < m and area[x][y + 1] == 1 and dfs(x, y + 1):
            return 1
        
        return 0
    
    return dfs(0, 0)

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

result = escape_possible(n, m, area)
print(result)