import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n = int(input()) # <=500
    board = [list(map(int, input().split())) for _ in range(n)]
    # 모든 칸에서 dfs를 돌려버리면 4^250000, 시간초과 -> dp로 각 칸마다 최대 4번만 비교해야 한다.
    # dp이용 -> 시간복잡도: 4*500*500 (백만)
    dp = [[-1]*n for _ in range(n)] # dp[i][j]: (i,j)까지 얻을 수 있는 최대 칸 수
    
    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]
        dp[x][y] = 1
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<n and board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
        return dp[x][y]
    
    for i in range(n):
        for j in range(n):
            dfs(i,j)
    print(max(max(row) for row in dp))
solution()