from collections import *

def bfs(grid,start,n,m):
    visited=[[False]*m for _ in range(n)]
    q=deque()
    q.append((start[0],start[1],0)) #0은 경로 카운트
    visited[start[0]][start[1]]=True
    directions=[(0,-1),(-1,0),(0,1),(1,0)]
    while q:
        curr,curc,curcount=q.popleft()
        if curr==n-1 and curc==m-1:
            return curcount
        for i in range(4):
           tempr=curr+directions[i][0]
           tempc=curc+directions[i][1]
           if 0<=tempr<n and 0<=tempc<m:
                if grid[tempr][tempc]==1 and visited[tempr][tempc]==False:
                    visited[tempr][tempc]==True
                    q.append((tempr,tempc,curcount+1))
    return -1



n,m=map(int,input().split())

lili=[list(map(int,input().split())) for _ in range(n)]

print(bfs(lili, (0,0),n,m))