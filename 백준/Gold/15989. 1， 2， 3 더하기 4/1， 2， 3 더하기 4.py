import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    ns = [int(input()) for _ in range(t)]
    max_n = max(ns)
    dp = [0]*(max_n+1)
    nums = [1, 2, 3]
    dp[0] = 1 # 0을 만드는 경우의 수는 없음 1개
    for num in nums:
        for i in range(num, max_n+1):
            dp[i] += dp[i-num]
    for n in ns:
        print(dp[n])
solution()