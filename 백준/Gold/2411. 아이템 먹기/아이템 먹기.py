import sys
import math
input = sys.stdin.readline

# 입력 처리
N, M, A, B = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(A)]
obstacles = set(tuple(map(int, input().split())) for _ in range(B))

# 시작점과 도착점 추가
points = [(1, 1)] + sorted(items) + [(N, M)]

# DP를 이용해 from -> to 경로의 수를 계산 (오른쪽/위쪽만 가능, 장애물 고려)
def count_paths(sx, sy, ex, ey):
    if (sx > ex or sy > ey):
        return 0

    dp = [[0] * (ey - sy + 1) for _ in range(ex - sx + 1)]

    for i in range(ex - sx + 1):
        for j in range(ey - sy + 1):
            x, y = sx + i, sy + j
            if (x, y) in obstacles:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[-1][-1]

# 전체 경로 수 = 각 경유지 구간별 경로 수를 곱한 것
result = 1
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    cnt = count_paths(x1, y1, x2, y2)
    if cnt == 0:
        result = 0
        break
    result *= cnt

print(result)
