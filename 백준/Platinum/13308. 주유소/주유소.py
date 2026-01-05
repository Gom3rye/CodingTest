import sys, heapq
from math import log2
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #도시 <=2500, #도로 <=4000
    gas = [0]+list(map(int, input().split())) # 1based index, 리터당 가격은 최대 2500
    graph = [[] for _ in range(n+1)]
    max_gas = max(gas)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    # 상태를 확장한 다익스트라!-> dp[i][j]: i노드에 j의 최소기름가격으로 도착한 비용
    INF = float('inf')
    dp = [[INF]*(max_gas+1) for _ in range(n+1)]
    q = []
    dp[1][gas[1]] = 0
    heapq.heappush(q, (0, 1, gas[1])) # dp[i][j], now, j
    while q:
        dist, now, min_price = heapq.heappop(q)
        if dist > dp[now][min_price]:
            continue
        for nxt, ndist in graph[now]:
            cost = dist+ndist*min_price
            nmin_price = min(min_price, gas[nxt])
            if cost < dp[nxt][nmin_price]:
                dp[nxt][nmin_price] = cost
                heapq.heappush(q, (cost, nxt, nmin_price))
    print(min(dp[n]))
solution()
