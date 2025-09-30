import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    INF = float('inf')
    dp = [INF]*n
    dp[0] = 0 # 시작 지점은 점프 0번 해도 된다.
    for i in range(n):
        if arr[i] == 0:
            continue
        # j만큼 점프를 할 수 있는지 확인
        for j in range(1, arr[i]+1):
            if i+j < n:
                dp[i+j] = min(dp[i+j], dp[i]+1)
    print(dp[-1] if dp[-1] != INF else -1)
solution()