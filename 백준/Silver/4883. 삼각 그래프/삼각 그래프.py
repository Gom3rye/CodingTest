import sys
from math import log2
input = sys.stdin.readline
INF = float('inf')
def solution():
    idx = 1
    while True:
        n = int(input()) # <=100,000
        if n == 0:
            break
        costs = [list(map(int, input().split())) for _ in range(n)]
        dp = [[0]*3 for _ in range(n)]
        # 0,1에서만 출발 가능하니까 아래와 같이 초기화
        dp[0][0] = INF
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][1]+costs[0][2]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])+costs[i][0]
            dp[i][1] = min(min(dp[i-1]), dp[i][0])+costs[i][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1])+costs[i][2]

        print(f"{idx}. {dp[-1][1]}")
        idx += 1
solution()
