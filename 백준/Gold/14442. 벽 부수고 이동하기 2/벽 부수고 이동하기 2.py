import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m, k = map(int, input().split()) # <=1000, <=1000, <=10
    board = [list(map(int, input().strip())) for _ in range(n)]
    q = deque([(0,0,0,1)])
    visited = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    while q:
        x, y, cnt, dist = q.popleft()
        if (x, y) == (n-1, m-1): # 가장 먼저 도착점에 도착한 길이가 최단 거리다!
            print(dist)
            return
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<m:
                # 각각 0인 경우와 1인 경우 나눠서 탐색해야 한다. (각각 상태가 달라지니까)
                if board[nx][ny] == 0 and not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = True
                    q.append((nx, ny, cnt, dist+1))
                elif board[nx][ny] == 1 and cnt+1 <= k and not visited[nx][ny][cnt+1]:
                    visited[nx][ny][cnt+1] = True
                    q.append((nx, ny, cnt+1, dist+1))
    print(-1)
solution()