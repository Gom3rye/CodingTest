import sys
input = sys.stdin.readline
def solution():
    n, m, h = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(h+1) for _ in range(n+1)] # dp[i][j]: i번째 학생이 j높이의 탑을 쌓은 경우
    dp[0][0] = 1 # 아무 학생이 아무 블록은 안 놓은 경우의 수
    for i in range(1, n+1):
        for j in range(h+1):
            dp[i][j] = dp[i-1][j] # 아무것도 안 놓은 경우의 수
            for b in blocks[i-1]:
                if j-b >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-b])%10007 # 아무것도 안 놓은 경우의 수 + 놓은 경우의 수

    print(dp[n][-1])
solution()