import sys
input = sys.stdin.readline
def solution():
    c, n = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]
    INF = float('inf')
    # c보다 약간 더 많은 고객을 유치하는 게 더 저렴할 수 있으니까 최대 고객 수가 될 수 있는 100에 +1을 넉넉히 해준다.)
    dp = [INF]*(c+101) # dp[i] = i고객을 유치하는데 필요한 최소 비용
    dp[0] = 0
    for cost, people in info:
        for i in range(people, c+101):
            dp[i] = min(dp[i], dp[i-people]+cost)
    # c명 이상 중 가장 작은 비용
    print(min(dp[c:]))
solution()