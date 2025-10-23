import sys
input = sys.stdin.readline
INF = sys.maxsize
n,k = map(int,input().split())
dist = []
dp = [[INF for _ in range(k+1)] for _ in range(n)]
for _ in range(n):
    dist.append(list(map(int,input().split())))
for i in range(k+1):
    dp[0][i] = 0
def mht(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for e in range(1,n):
    for cost in range(k+1):
        if e-cost < 0:
            break
        for curr in range(cost,k+1):
            dp[e][curr] = min(dp[e-cost-1][curr-cost] + mht(dist[e],dist[e-cost-1]), dp[e][curr])

print(dp[n-1][k])