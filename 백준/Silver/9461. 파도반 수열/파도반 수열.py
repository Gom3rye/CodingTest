import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input()) # <= 100
        dp = [1]*(n+1)
        for i in range(3, n+1):
            dp[i] = dp[i-3]+dp[i-2]
        print(dp[n-1])
solution()