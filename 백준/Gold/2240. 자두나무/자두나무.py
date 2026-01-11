import sys
input = sys.stdin.readline
def solution():
    t, w = map(int, input().split()) # 초 <=1000, 최대 움직임 횟수 <=30
    plums = [0]+[int(input()) for _ in range(t)] # 1based index
    dp = [[0]*(w+1) for _ in range(t+1)]
    for i in range(1, t+1):
        for j in range(w+1):
            # 안 움직이는 경우
            dp[i][j] = dp[i-1][j]

            # 움직이는 경우
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])

            tree = 1 if j%2==0 else 2 # 짝수면 1그대로, 홀수면 2로 이동
            if tree == plums[i]:
                dp[i][j] += 1
    print(max(dp[-1]))
solution()