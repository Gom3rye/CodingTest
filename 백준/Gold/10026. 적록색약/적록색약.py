import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    # 비적록색약, 적록색약(R=G)
    board = [list(input().strip()) for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def bfs(x, y):
        q = deque([(x, y)])
        color = board[x][y]
        visited[x][y] = True
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    count = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                count += 1

    count2 = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 'B':
                board[i][j] = 'A'
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                count2 += 1
    print(count, count2)
solution()