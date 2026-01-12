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
        # 0,1에서만 출발 가능하니까 아래와 같이 초기화
        dp = [INF, costs[0][1], costs[0][1]+costs[0][2]]
        for i in range(1, n):
            new_dp = [0]*3
            left, mid, right = costs[i]
            new_dp[0] = min(dp[0], dp[1])+left
            new_dp[1] = min(min(dp), new_dp[0])+mid
            new_dp[2] = min(dp[1], dp[2], new_dp[1])+right
            # 한 줄씩 갱신
            dp = new_dp
        print(f"{idx}. {dp[1]}")
        idx += 1
solution()