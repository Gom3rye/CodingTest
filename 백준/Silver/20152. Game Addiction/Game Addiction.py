import sys
input = sys.stdin.readline
def solution():
    H, N = map(int, input().split())
    d = abs(N - H)
    if d == 0:
        print(1)
        return
    
    dp = [[0]*(d+1) for _ in range(d+1)]
    dp[0][0] = 1
    
    for i in range(d+1):
        for j in range(d+1):
            if j > i:  # 침수 지역
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                continue
            ways_from_left = dp[i-1][j] if i > 0 else 0
            ways_from_up = dp[i][j-1] if j > 0 else 0
            dp[i][j] = ways_from_left + ways_from_up
    
    print(dp[d][d])
solution()