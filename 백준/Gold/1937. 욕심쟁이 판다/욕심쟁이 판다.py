import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n = int(input())
    bamboo = [list(map(int, input().split())) for _ in range(n)]
    # dfs로 가장 큰 덩어리 구하기 문제
    # But, 시작점을 모르니까 bruteforce로 하되 시간 초과 나지 않기 위해서 memoization을 해야 한다.
    dp = [[-1]*n for _ in range(n)] # dp[i][j]: (i,j)까지 가는 최대 덩어리 수
    def dfs(x, y):
        # memoization
        if dp[x][y] != -1:
            return dp[x][y]
        
        dp[x][y] = 1
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<n and bamboo[nx][ny] > bamboo[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)

        return dp[x][y]
    max_count = 0
    for i in range(n):
        for j in range(n):
            max_count = max(max_count, dfs(i,j))
    print(max_count)
solution()