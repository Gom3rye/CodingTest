import sys
input = sys.stdin.readline

T, A, B = map(int, input().split())

# dp[i] = 물 마시기 전, 포만감 i 가능?
dp = bytearray(T + 1)
dp[0] = 1

# 1️⃣ 물 마시기 전 DP
for i in range(T + 1):
    if dp[i]:
        if i + A <= T:
            dp[i + A] = 1
        if i + B <= T:
            dp[i + B] = 1

# dp2[i] = 물 마신 후, 포만감 i 가능?
dp2 = bytearray(T + 1)

# 2️⃣ 물을 한 번 마신 상태 세팅
for i in range(T + 1):
    if dp[i]:
        dp2[i // 2] = 1

# 3️⃣ 물 마신 후 DP
for i in range(T + 1):
    if dp2[i]:
        if i + A <= T:
            dp2[i + A] = 1
        if i + B <= T:
            dp2[i + B] = 1

# 4️⃣ 최대 포만감 찾기
ans = 0
for i in range(T + 1):
    if dp[i] or dp2[i]:
        ans = i

print(ans)
