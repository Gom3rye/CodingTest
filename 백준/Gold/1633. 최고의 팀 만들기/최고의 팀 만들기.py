import sys
input = sys.stdin.readline
def solution():
    players = []
    while True:
        try:
            w, b = map(int, input().split())
            players.append((w, b))
        except:
            break
    dp = [[0]*16 for _ in range(16)] # dp[i][j]: 백i명, 흑j명 뽑았을 때 최대 능력
    for w, b in players:
        for i in range(15, -1, -1):
            for j in range(15, -1, -1):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j]+w)
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1]+b)
    print(dp[-1][-1])
solution()