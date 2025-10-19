import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    MOD = 1000000000
    # k개로 n의 수를 만드는 경우의 수
    dp = [[0]*(n+1) for _ in range(k+1)] # dp[i][j]: i개로 j를 만드는 경우의 수
    for i in range(1, n+1):
        dp[1][i] = 1
    for i in range(1, k+1):
        dp[i][1] = i # i개로 1을 만드는 경우의 수 001 010 100
    for i in range(2, k+1):
        for j in range(2, n+1):
            dp[i][j] += (dp[i-1][j]+dp[i][j-1])%MOD
    print(dp[-1][-1])
solution()