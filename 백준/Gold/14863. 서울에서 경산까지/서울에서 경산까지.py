import sys

# go : 현재 idx번째 경로에서 남은 시간이 total일 때 얻을 수 있는 최대 모금액을 리턴하는 함수
def go(idx, total):
    # 시간 예외 처리
    if total < 0:
        return -9876543210
    # Base case : 경산까지 도달한 경우
    if idx == n:
        return 0
    # Memoization
    if dp[idx][total] != -1:
        return dp[idx][total]
    # 점화식
    dp[idx][total] = max(go(idx + 1, total - arr[idx][0]) + arr[idx][1], go(idx + 1, total - arr[idx][2]) + arr[idx][3])
    return dp[idx][total]

# 입력부 및 정답출력
n, k = map(int, sys.stdin.readline().split())
dp = [[-1] * (k + 1) for _ in range(n)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(go(0, k))