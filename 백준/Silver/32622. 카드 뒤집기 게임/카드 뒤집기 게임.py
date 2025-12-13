import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 1️⃣ 뒤집지 않는 경우: 원래 배열의 최장 연속 구간
max_orig = 1
cur = 1
for i in range(1, N):
    if A[i] == A[i-1]:
        cur += 1
    else:
        max_orig = max(max_orig, cur)
        cur = 1
max_orig = max(max_orig, cur)

# 2️⃣ suffix 연속 길이 계산
suffix0 = [0] * (N + 2)
suffix1 = [0] * (N + 2)

for i in range(N - 1, -1, -1):
    if A[i] == 0:
        suffix0[i] = suffix0[i + 1] + 1
        suffix1[i] = 0
    else:
        suffix1[i] = suffix1[i + 1] + 1
        suffix0[i] = 0

# 3️⃣ prefix 뒤집기 + suffix 연결
ans = max_orig
prefix_len = 0

for i in range(N):
    if i == 0 or A[i] != A[i - 1]:
        prefix_len = 1
    else:
        prefix_len += 1

    flipped_color = 1 - A[i]      # i까지 뒤집었을 때 마지막 색
    if i + 1 < N:
        if A[i + 1] == flipped_color:
            if flipped_color == 0:
                ans = max(ans, prefix_len + suffix0[i + 1])
            else:
                ans = max(ans, prefix_len + suffix1[i + 1])
    else:
        # i == N-1 인 경우 (전체 뒤집기)
        ans = max(ans, prefix_len)

print(ans)
