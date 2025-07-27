import sys
input = sys.stdin.readline
def solution():
    # LIC을 구하는 문제!
    n = int(input())
    children = list(int(input()) for _ in range(n))
    dp = [1]*(n+1)
    for i in range(1, n):
        for j in range(i):
            if children[i] > children[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(n-max(dp))
solution()