import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    snacks = [int(input()) for _ in range(n)]
    dp = [0]*n # dp[i]: i번 날 간식 최대 만족도
    dp[0] = snacks[0]
    for i in range(1, n):
        dp[i] = snacks[i] # i번째 snack부터 시작
        for j in range(i):
            if snacks[i] > snacks[j]:
                dp[i] = max(dp[i], dp[j]+snacks[i])
    print(max(dp))
solution()