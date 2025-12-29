import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    m, n = map(int, input().split()) # 세로, 가로 <=500
    board = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1]*n for _ in range(m)] # dp[i][j]: 0,0~i,j까지 갈 수 있는 경로의 개수
    def dfs(x, y):
        if (x, y) == (m-1, n-1):
            return 1
        if dp[x][y] != -1: # memoization
            return dp[x][y]
        dp[x][y] = 0
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = dx+x, dy+y
            if not (0<=nx<m and 0<=ny<n):
                continue
            if board[x][y] > board[nx][ny]:
                dp[x][y] += dfs(nx, ny)
        return dp[x][y]
    dfs(0, 0)
    print(dp[0][0])
solution()