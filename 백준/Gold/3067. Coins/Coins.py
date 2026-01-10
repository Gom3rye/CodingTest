import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input()) # #동전 <=20
        coins = list(map(int, input().split()))
        target = int(input())
        dp = [0]*(target+1) # dp[target]: target을 만들 수 있는 방법의 수
        dp[0] = 1
        for c in coins:
            for now in range(c, target+1):
                dp[now] += dp[now-c]
        print(dp[target])
solution()