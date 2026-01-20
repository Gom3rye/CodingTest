import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # <=300
    jx, jy, tx, ty = map(int, input().split())
    jx -= 1
    jy -= 1
    tx -= 1
    ty -= 1 # 0based index
    board = [list(input().strip()) for _ in range(n)]
    q = deque([(jx, jy)])
    dist = [[-1]*m for _ in range(n)]
    dist[jx][jy] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (tx, ty):
            print(dist[x][y])
            return

        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if not (0<=nx<n and 0<=ny<m):
                continue
            if dist[nx][ny] != -1:
                continue
            if board[nx][ny] == '0':
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx, ny))
            else: # 친구나 타겟을 만난 경우
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))
                
solution()