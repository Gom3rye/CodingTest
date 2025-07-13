import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    n, m, k = map(int, input().split())
    lake = [[0]*m for _ in range(n)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for _ in range(k):
        r, c = map(int, input().split())
        lake[r-1][c-1] = 1

    def dfs(x, y):
        lake[x][y] = 0 # 방문 처리
        lake_size = 1
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and lake[nx][ny] == 1: 
                lake[nx][ny] = 0 # 방문 처리
                lake_size += dfs(nx, ny)
        return lake_size
    
    largest_lake = 0
    for i in range(n):
        for j in range(m):
            if lake[i][j] == 1:
                largest_lake = max(largest_lake, dfs(i,j))

    print(largest_lake)
solution()