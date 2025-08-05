import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 같은 방향으로 두 번 연속 움직일 수 없으므로 상태 관리해서 dp로 풀기
    INF = float('inf')
    dp = [[[INF, INF, INF] for _ in range(m)] for _ in range(n)] 
    # dp[x][y][0]: (x,y)로 좌하향으로 온 경우
    # dp[x][y][1]: (x,y)로 직선으로 내려 온 경우
    # dp[x][y][2]: (x,y)로 우하향으로 온 경우
    for j in range(m):
        dp[0][j][0] = dp[0][j][1] = dp[0][j][2] = board[0][j]
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2])+board[i][j]
                dp[i][j][1] = dp[i-1][j][0] + board[i][j]
            elif j < m-1:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2])+board[i][j]
                dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2])+board[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1])+board[i][j]
            elif j == m-1:
                dp[i][j][1] = dp[i-1][j][2] + board[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1])+board[i][j]
    min_cost = INF
    for i in range(m):
        cost = dp[n-1][i]
        min_cost = min(min_cost, min(cost))
    print(min_cost)
solution()