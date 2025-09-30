import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    INF = float('inf')
    dp = [INF]*n # dp[i]: 0번 돌에서 i번 돌까지 가는 최소 비용
    dp[0] = 0 # 시작점 비용은 0
    for i in range(n):
        for j in range(i+1, n):
            k = (j-i)*(1+abs(arr[i]-arr[j]))
            dp[j] = min(dp[j], max(dp[i], k))
    print(dp[-1])
solution()