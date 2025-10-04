import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 상승과 하강이 다른 방향이므로 dp 따로 정의
    INF = float('inf')
    # (n-1, 0) ~ (i, j)
    up_dp = [[-INF]*m for _ in range(n)]
    # (n-1, m-1) ~ (i, j)
    down_dp = [[-INF]*m for _ in range(n)]
    up_dp[n-1][0] = board[n-1][0] # 초기화
    down_dp[n-1][m-1] = board[n-1][m-1] # 초기화
    # up
    for i in range(n-1, -1, -1):
        for j in range(m):
            if i > 0:
                up_dp[i-1][j] = max(up_dp[i-1][j], up_dp[i][j]+board[i-1][j])
            if j+1 < m:
                up_dp[i][j+1] = max(up_dp[i][j+1], up_dp[i][j]+board[i][j+1])
    # down
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i > 0:
                down_dp[i-1][j] = max(down_dp[i-1][j], down_dp[i][j]+board[i-1][j])
            if j > 0:
                down_dp[i][j-1] = max(down_dp[i][j-1], down_dp[i][j]+board[i][j-1])
    
    # 총합이 가장 큰 경우 구하기
    answer = -INF
    for i in range(n):
        for j in range(m):
            score = up_dp[i][j]+down_dp[i][j]
            answer = max(answer, score)
    print(answer)
solution()