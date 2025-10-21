scroll = input().strip()
devil = input().strip()
angel = input().strip()

N = len(scroll)
L = len(devil)

dp = [[[0]*2 for _ in range(L)] for _ in range(N)]
prefix_sum = [[[0]*L for _ in range(2)] for _ in range(N)]

# 초기화
for j in range(L):
    if devil[j] == scroll[0]:
        dp[0][j][0] = 1
    if angel[j] == scroll[0]:
        dp[0][j][1] = 1

    # 누적합 초기화
    prefix_sum[0][0][j] = dp[0][j][0] + (prefix_sum[0][0][j-1] if j > 0 else 0)
    prefix_sum[0][1][j] = dp[0][j][1] + (prefix_sum[0][1][j-1] if j > 0 else 0)

# DP + 누적합 계산
for i in range(1, N):
    for j in range(L):
        if devil[j] == scroll[i]:
            dp[i][j][0] = prefix_sum[i-1][1][j-1] if j > 0 else 0
        if angel[j] == scroll[i]:
            dp[i][j][1] = prefix_sum[i-1][0][j-1] if j > 0 else 0

    # 누적합 갱신
    for j in range(L):
        prefix_sum[i][0][j] = dp[i][j][0] + (prefix_sum[i][0][j-1] if j > 0 else 0)
        prefix_sum[i][1][j] = dp[i][j][1] + (prefix_sum[i][1][j-1] if j > 0 else 0)

# 정답 계산
result = 0
for j in range(L):
    result += dp[N-1][j][0] + dp[N-1][j][1]

print(result)