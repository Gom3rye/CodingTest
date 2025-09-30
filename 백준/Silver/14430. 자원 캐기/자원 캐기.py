import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = board[0][0]

    # 첫 행
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + board[0][j]

    # 첫 열
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + board[i][0]

    # 나머지
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + board[i][j]

    print(dp[n-1][m-1])

solution()
