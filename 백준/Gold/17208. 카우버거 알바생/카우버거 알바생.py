N, M, K = map(int, input().split())  # 주문 수, 치즈버거 수, 감자튀김 수
orders = [tuple(map(int, input().split())) for _ in range(N)]

# dp[치즈버거][감자튀김] = 최대 주문 수
dp = [[0] * (K + 1) for _ in range(M + 1)]

for x, y in orders:
    for i in range(M, x - 1, -1):
        for j in range(K, y - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)

# 최대 주문 수 찾기
answer = 0
for i in range(M + 1):
    for j in range(K + 1):
        answer = max(answer, dp[i][j])

print(answer)