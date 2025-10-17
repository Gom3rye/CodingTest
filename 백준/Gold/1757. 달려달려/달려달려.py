import sys
input = sys.stdin.readline

n,m = map(int, input().split())
D = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n)]


dp[0][1] = D[0]
if n > 1:
    dp[1][0] = D[0]
for i in range(1,n):
    dp[i][0] = max(dp[i][0], dp[i-1][0]) # 계속 쉬는 경우도 고려
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j-1] + D[i], dp[i][j])
        if i+j < n:
            dp[i+j][0] = max(dp[i+j][0], dp[i][j]) # 여기서 휴식 하기로 결정, 지침지수가 0이 될때까지 무조건 휴식

ans = 0
for i in range(n):
    for j in range(m+1):
        if j <= n-i-1: # 해당 시점에서 n분이 끝났을때까지 지침지수가 0이 달성될 수 있어야함
            ans = max(ans, dp[i][j])
print(ans)

# n분이 주어짐, 그 시간동안 달릴지 쉴지를 결정할 수 있음
# 1분 뛰면 지침지수 1 증가, 1분 쉬면 지침지수 1 감소
# 지침지수가 m보다 커지면 더이상 달리는거 불가능(완전 stop)
# I분때 달리면 Di만큼의 거리를 달릴 수 있음
# 한번 쉬면 지침지수가 0이 될때까지 쭉 쉬어야함
# 달리기가 끝났을때 지침지수가 0이 되어야함
# 최대로 멀리갈 수 있는 거리?

# 현재 시점에서 더 뛰거나, 휴식을 결정하거나