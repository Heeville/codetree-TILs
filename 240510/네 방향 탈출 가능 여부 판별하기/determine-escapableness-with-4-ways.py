from collections import deque

def escape_possible(n, m, area):
    # 상, 하, 좌, 우 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐 생성 및 시작점 설정
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        # 우측 하단에 도달하면 탈출 가능
        if x == n - 1 and y == m - 1:
            return 1
        
        # 현재 위치에서 상, 하, 좌, 우로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위를 벗어나거나 뱀이 있는 곳이면 스킵
            if nx < 0 or nx >= n or ny < 0 or ny >= m or area[nx][ny] == 0:
                continue
            
            # 방문한 곳을 표시하고 큐에 추가
            area[nx][ny] = 0
            queue.append((nx, ny))
    
    # 큐를 모두 탐색했는데 우측 하단에 도달하지 못한 경우 탈출 불가능
    return 0

# 입력 받기
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

# 함수 호출 및 결과 출력
result = escape_possible(n, m, area)
print(result)