import sys
input = sys.stdin.readline

# DP 테이블을 미리 계산해 둠
# dp[i][j]: i자리 수이면서 j로 끝나는 줄어들지 않는 수의 개수
dp = [[0] * 10 for _ in range(65)]

# Base Case: 1자리 수인 경우, 각 숫자로 끝나는 경우는 1개씩
for i in range(10):
    dp[1][i] = 1

# 2자리부터 64자리까지 DP 테이블 채우기
for i in range(2, 65):
    for j in range(10):
        # j로 끝나는 i자리 수의 개수는,
        # (j-1)로 끝나는 i자리 수의 개수 + j로 끝나는 (i-1)자리 수의 개수
        # (j=0일 때는 j-1이 없으므로, j로 끝나는 (i-1)자리 수의 개수와 동일)
        for k in range(j + 1):
            dp[i][j] += dp[i-1][k]

def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        # n자리 수의 총개수는, n자리 수이면서 0~9로 끝나는 모든 경우의 합
        print(sum(dp[n]))

solution()