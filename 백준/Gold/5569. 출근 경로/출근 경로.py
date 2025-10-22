import sys
input = sys.stdin.readline
def solution():
    w, h = map(int, input().split())
    MOD = 100000
    # 오른쪽, 위쪽으로만 이동 가능 - 출근할 수 있는 총 경로의 수 %MOD
    # 조건: 방향을 바꾼 후 1블록만 이동한 후 다시 방향을 바꿀 수 없다.
    # dp 상태 정의: dp[h][w][state] 0:오오, 1:위오, 2:위위, 3:오위
    # 오위: 직전에 오른쪽으로 갔고 지금 위쪽으로 간다.
    dp = [[[0]*(4) for _ in range(w+1)] for _ in range(h+1)]
    # 초기화
    for i in range(2, w+1): # (1,1)에서 (1,2)...(1,w)로 가는 경우
        dp[1][i][0] = 1 # 오오
    for j in range(2, h+1): # (1,1)에서 (2,1)...(h,1)로 가는 경우
        dp[j][1][2] = 1 # 위위

    for i in range(2, h+1):
        for j in range(2, w+1):
            # i,j로 오오 로 도착하려면
            dp[i][j][0] = (dp[i][j-1][0]+dp[i][j-1][1])%MOD
            dp[i][j][1] = dp[i][j-1][2]%MOD
            dp[i][j][2] = (dp[i-1][j][2]+dp[i-1][j][3])%MOD
            dp[i][j][3] = dp[i-1][j][0]%MOD
    print(sum(dp[-1][-1])%MOD)
solution()