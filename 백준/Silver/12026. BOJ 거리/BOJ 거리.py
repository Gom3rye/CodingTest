INF = float('inf')

N = int(input())
board = input().strip()

# B -> 0, O -> 1, J -> 2 로 매핑
def next_char(c):
    return {'B': 'O', 'O': 'J', 'J': 'B'}[c]

dp = [INF] * N
dp[0] = 0  # 시작점

for i in range(N):
    for j in range(i + 1, N):
        if board[j] == next_char(board[i]):
            cost = (j - i) ** 2
            dp[j] = min(dp[j], dp[i] + cost)

# 결과
print(dp[N - 1] if dp[N - 1] != INF else -1)
