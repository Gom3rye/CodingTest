import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    # 이전 결과값을 가져와서 사용하면 3중 for문 안 돌려도 되니까 dp 사용하자.
    dp = [[0]*m for _ in range(n)] # dp[i][j] = (i,j)를 오른쪽 아래 꼭짓점으로 가지는 정사각형의 한 변의 최대 길이

    for i in range(n):
        for j in range(m):
            if board[i][j] == '1':
                if i==0 or j==0:
                    dp[i][j] = 1
                else: # i>=1 and j>=1
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
    print(max(max(row) for row in dp)**2)
solution()