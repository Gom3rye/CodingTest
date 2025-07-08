import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = [[0]*m for _ in range(n)]  # 0: unvisited, 1: visiting, 2: finished

    def dfs(x, y, px, py):
        visited[x][y] = 1  # visiting

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) == (px, py):
                    continue
                if board[nx][ny] != board[x][y]:
                    continue
                if visited[nx][ny] == 1:
                    print("Yes")
                    sys.exit()
                if visited[nx][ny] == 0:
                    dfs(nx, ny, x, y)
        visited[x][y] = 2  # finished

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                dfs(i, j, -1, -1)
    print("No")
solution()