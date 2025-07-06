import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    n, m = map(int, input().split()) # 가로, 세로
    war = [input().strip() for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def dfs(x, y):
        nonlocal count
        visited[x][y] = True
        count += 1
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny] and war[x][y] == war[nx][ny]:
                    dfs(nx, ny)
        return count
    
    our_team = 0
    opponent = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                count = 0
                if war[i][j] == 'W':
                    our_team += dfs(i,j)**2
                else:
                    opponent += dfs(i,j)**2
    print(our_team, opponent)
solution()