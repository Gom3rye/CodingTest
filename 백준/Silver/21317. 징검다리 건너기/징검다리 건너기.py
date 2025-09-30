import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    jumps = [list(map(int, input().split())) for _ in range(n-1)]
    k = int(input())
    INF = float('inf')
    dp = [[INF]*2 for _ in range(n)] # dp[i][0]:k 미사용한 후 에너지, dp[i][1]:k 사용한 후 에너지
    dp[0][0] = 0
    for i in range(n):
        for j in range(2):
            # 작은 점프
            if i+1<n:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+jumps[i][0])
            # 큰 점프
            if i+2<n:
                dp[i+2][j] = min(dp[i+2][j], dp[i][j]+jumps[i][1])
            # 매우 큰 점프
            if j == 0 and i+3<n:
                dp[i+3][1] = min(dp[i+3][1], dp[i][j]+k)
    print(min(dp[-1]))
solution()