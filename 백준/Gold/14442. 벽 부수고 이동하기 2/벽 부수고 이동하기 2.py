import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m, k = map(int, input().split()) # <=1000, <=1000, <=10
    board = [list(map(int, input().strip())) for _ in range(n)]
    q = deque([(0,0,0)])
    distance = [[[INF]*(k+1) for _ in range(m)] for _ in range(n)]
    distance[0][0][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (n-1, m-1):
            print(distance[x][y][cnt])
            return
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 0 and distance[nx][ny][cnt] == INF:
                    distance[nx][ny][cnt] = distance[x][y][cnt]+1
                    q.append((nx, ny, cnt))
                elif board[nx][ny] == 1 and cnt+1 <= k and distance[nx][ny][cnt+1] == INF:
                    distance[nx][ny][cnt+1] = distance[x][y][cnt]+1
                    q.append((nx, ny, cnt+1))
    print(-1)
solution()