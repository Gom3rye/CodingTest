import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # <=1000
    board = [list(map(int, input().split())) for _ in range(n)]
    INF = float('inf')
    dp = [[-INF]*m for _ in range(n)]
    dp[0][0] = board[0][0]
    # 왼쪽 <-> 오른쪽 의존성 순환문제 발생 가능 => 각각 따로 계산해줘서 나중에 합치기 (동시에 계산x)
    # i==0일때
    for j in range(1, m):
        dp[0][j] = dp[0][j-1]+board[0][j]

    for i in range(1, n):
        left = [-INF]*m
        right = [-INF]*m
        # 위에서 아래로
        for j in range(m):
            dp[i][j] = dp[i-1][j]+board[i][j]
        # 왼 -> 오
        left[0] = dp[i][0]
        for j in range(1, m):
            left[j] = max(left[j-1], dp[i-1][j])+board[i][j]
        # 오 -> 왼
        right[m-1] = dp[i][m-1]
        for j in range(m-2, -1, -1):
            right[j] = max(right[j+1], dp[i-1][j])+board[i][j]
        # left, right 합쳐서 고려
        for j in range(m):
            dp[i][j] = max(left[j], right[j])
    print(dp[-1][-1])
solution()