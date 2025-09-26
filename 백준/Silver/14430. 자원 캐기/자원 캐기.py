import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# --- 입력 처리 ---
N, M = map(int, input().split())

# DP 테이블과 광석 정보를 저장할 그리드
# (N+1) x (M+1) 크기로 만들어 0-based 인덱싱의 번거로움을 피함
grid = [[0] * (M + 1)]
for _ in range(N):
    grid.append([0] + list(map(int, input().split())))

# dp[i][j]: (1,1)에서 (i,j)까지 이동하며 얻는 최대 자원 수
dp = [[0] * (M + 1) for _ in range(N + 1)]

# --- DP 계산 ---
# (1,1)부터 (N,M)까지 순회하며 DP 테이블을 채움
for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 위쪽에서 오는 경우와 왼쪽에서 오는 경우 중 더 큰 값을 선택하고,
        # 현재 위치의 자원을 더함
        max_from_prev = max(dp[i-1][j], dp[i][j-1])
        dp[i][j] = max_from_prev + grid[i][j]

# 최종 목적지 (N, M)에 저장된 값이 정답
print(dp[N][M])