import sys
from collections import deque
input = sys.stdin.readline
def solution():
    r, c = map(int, input().split()) # <=50
    board = [list(input().strip()) for _ in range(r)]
    water = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                sx, sy = i, j
            elif board[i][j] == 'D':
                ex, ey = i, j
            elif board[i][j] == '*':
                water.append((i, j))
    # *:물, X:돌, .:빈곳
    hq = deque([(sx, sy)])
    h_dist = [[-1]*c for _ in range(r)]
    h_dist[sx][sy] = 0
    wq = deque(water)
    w_dist = [[-1]*c for _ in range(r)]
    for i, j in water:
        w_dist[i][j] = 0
    # water부터 움직이기
    while wq:
        x, y = wq.popleft()
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if not (0<=nx<r and 0<=ny<c):
                continue
            if board[nx][ny] == 'X' or board[nx][ny] == 'D':
                continue
            if w_dist[nx][ny] == -1:
                w_dist[nx][ny] = w_dist[x][y]+1
                wq.append((nx, ny))
    # hedgehog 움직이기
    while hq:
        x, y = hq.popleft()
        if (x, y) == (ex, ey):
            print(h_dist[x][y])
            return
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if not (0<=nx<r and 0<=ny<c):
                continue
            if board[nx][ny] == 'X' or board[nx][ny] == '*':
                continue
            if h_dist[nx][ny] == -1:
                h_dist[nx][ny] = h_dist[x][y]+1
                if (h_dist[nx][ny] < w_dist[nx][ny]) or w_dist[nx][ny] == -1:
                    hq.append((nx, ny))
    print("KAKTUS")
solution()