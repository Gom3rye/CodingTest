import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 방문 처리 겸 거리 저장
    distance = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 1:
                if board[i][j] == 2:
                    sx, sy = i, j
                distance[i][j] = 0
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    for row in distance:
        print(*row)
solution()