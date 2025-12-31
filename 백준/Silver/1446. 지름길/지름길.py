n, d = map(int, input().split())
short_road = [list(map(int, input().split())) for _ in range(n)]

dp = [1e9] * (d+1)
dp[0] = 0
for i in range(1, d+1):
    dp[i] = dp[i - 1] + 1
    for start, end, length in short_road:
        if i == end: # (1)
            dp[i] = min(dp[i], dp[start]+length)

print(dp[d])