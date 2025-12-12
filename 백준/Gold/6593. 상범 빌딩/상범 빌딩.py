import sys
from collections import deque
input = sys.stdin.readline
def solution():
    while True:
        l, r, c = map(int, input().split()) # 상범 빌딩의 층수, 행, 열
        if (l, r, c) == (0, 0, 0):
            break

        board = []
        for _ in range(l):
            floor = [list(input().strip()) for _ in range(r)]
            tmp = input().strip()
            board.append(floor)

        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if board[i][j][k] == 'S':
                        sz, sx, sy = i, j, k
                    elif board[i][j][k] == 'E':
                        ez, ex, ey = i, j, k
        
        directions = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(-1,0,0),(1,0,0)]
        q = deque([(sz, sx, sy)])
        distance = [[[-1]*c for _ in range(r)] for _ in range(l)]
        distance[sz][sx][sy] = 0
        while q:
            z, x, y = q.popleft()
            if (z, x, y) == (ez, ex, ey):
                print(f"Escaped in {distance[z][x][y]} minute(s).")
                break
            for dz, dx, dy in directions:
                nz, nx, ny = dz+z, dx+x, dy+y
                if 0<=nz<l and 0<=nx<r and 0<=ny<c and board[nz][nx][ny] != '#' and distance[nz][nx][ny] == -1:
                    distance[nz][nx][ny] = distance[z][x][y]+1
                    q.append((nz, nx, ny))
        else:
            print("Trapped!")

solution()