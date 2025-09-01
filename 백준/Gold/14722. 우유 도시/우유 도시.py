import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 딸->초->바->딸 (0->1->2->0)
    dp = [[0]*(n+1) for _ in range(n+1)] # dp[i][j]: (i-1, j-1)까지 마신 최대 개수
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            # dp[i][j]는 왼쪽에서 온 최대 개수, 위에서 온 최대 개수 중 더 큰 것 (안 먹었을 경우)
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # 먹었을 경우
            if dp[i][j]%3 == board[i-1][j-1]: # board는 0based index
                dp[i][j] += 1
    print(dp[-1][-1])
solution()