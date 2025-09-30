import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)] # i,j까지 오면서 얻을 수 있는 최대 자원 수
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])+board[i-1][j-1]
    print(dp[-1][-1])
solution()