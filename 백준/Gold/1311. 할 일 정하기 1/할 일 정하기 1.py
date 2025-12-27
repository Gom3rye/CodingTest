import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]

    INF = 10**15
    dp = [INF] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        person = bin(mask).count('1')
        if person >= n:
            continue

        for job in range(n):
            if not (mask & (1 << job)):
                next_mask = mask | (1 << job)
                dp[next_mask] = min(
                    dp[next_mask],
                    dp[mask] + cost[person][job]
                )

    print(dp[(1 << n) - 1])

solution()
