import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 표의 크기, 합을 구해야 하는 횟수
    board = [list(map(int, input().split())) for _ in range(n)]
    # dp[i][j]: (1,1)에서 (i,j)까지의 합
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            val = board[i-1][j-1]
            dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1] + val
    # print(dp)
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
solution()