import sys
input = sys.stdin.readline
def solution():
    m, n = map(int, input().split()) # 세로, 가로
    board = [list(map(int, input().split())) for _ in range(m)]
    # 1이나 2가 없는 최대한 큰 정사각형 변의 길이 구하기
    dp = [[0]*n for _ in range(m)] # i,j를 오른쪽 꼭짓점으로 하는 정사각형 최대 변 길이 
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
    print(max(max(row) for row in dp))
solution()