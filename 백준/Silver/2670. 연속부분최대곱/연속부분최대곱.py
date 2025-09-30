import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(float(input()) for _ in range(n))
    dp = [1]*n
    dp[0] = arr[0]
    for i in range(n):
        dp[i] = max(dp[i-1]*arr[i], arr[i])
    print(f"{max(dp):.3f}")
solution()