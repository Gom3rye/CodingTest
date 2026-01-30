import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    o1, o2 = map(int, input().split())
    m = int(input())
    doors = [int(input()) for _ in range(m)]

    INF = 10**9
    dp = [[[INF]*(n+1) for _ in range(n+1)] for _ in range(m+1)]

    dp[0][o1][o2] = 0

    for i in range(m):
        target = doors[i]
        for a in range(1, n+1):
            for b in range(1, n+1):
                if dp[i][a][b] == INF:
                    continue

                # a를 이동
                dp[i+1][target][b] = min(
                    dp[i+1][target][b],
                    dp[i][a][b] + abs(a - target)
                )

                # b를 이동
                dp[i+1][a][target] = min(
                    dp[i+1][a][target],
                    dp[i][a][b] + abs(b - target)
                )

    print(min(map(min, dp[m])))
solution()