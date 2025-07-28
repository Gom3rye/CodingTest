import sys
input = sys.stdin.readline
def solution():
    # 하, 우, 대각선만 이동 가능
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)] # dp[i][j]: (i,j)에서 가져갈 수 있는 최대의 사탕 개수
    for i in range(n):
        for j in range(m):
            from_top = dp[i-1][j] if 0<=i-1 else 0
            from_left = dp[i][j-1] if 0<=j-1 else 0
            from_diag = dp[i-1][j-1] if 0<=i-1 and 0<=j-1 else 0
            dp[i][j] = max(from_top, from_left, from_diag)+ board[i][j]
    print(dp[n-1][m-1])
solution()