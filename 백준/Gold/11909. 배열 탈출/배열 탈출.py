# 접근 방법
# 작은 숫자의 행부터 하나씩 탐색해나가며 (현재 행 - 1, 현재 열)까지 움직이는 데 든 돈과 해당 위치에서 현재 위치까지 움직이는 데 든 돈을 합한 것과 (현재 행, 현재 열 - 1)까지 움직이는 데 든 돈과 현재 위치까지 움직이는데 든 돈을 합한 것을 비교해 작은 값으로 갱신한다.
# 가장 마지막 열에 도달했을 때 거기까지 이동하기 위해 든 비용을 계산해 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n):
    for c in range(n):
        if 0>r-1 and 0>c-1:
            continue
        prev_r, prev_c = int(1e7), int(1e7)
        if 0<=r-1:
            prev_r = dp[r-1][c] + (0 if arr[r][c] < arr[r-1][c] else arr[r][c] - arr[r-1][c] + 1)
        if 0<=c-1:
            prev_c = dp[r][c-1] + (0 if arr[r][c] < arr[r][c-1] else arr[r][c] - arr[r][c-1] + 1)
        dp[r][c] = min(prev_r, prev_c)
print(dp[n-1][n-1])