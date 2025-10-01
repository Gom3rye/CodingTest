import sys
input = sys.stdin.readline
def solution():
    while True:
        n = int(input())
        if n == 0:
            break
        income = [int(input()) for _ in range(n)]
        dp = [0]*n # dp[i]: i까지의 최고 합
        dp[0] = income[0]
        for i in range(1, n):
            # 그 전까지 income을 가지고 오거나 새로 income 파거나
            dp[i] = max(income[i], dp[i-1]+income[i])
        print(max(dp))
solution()