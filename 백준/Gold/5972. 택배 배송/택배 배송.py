import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #헛간, #길 <=50,000
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    INF = float('inf')
    q = []
    heapq.heappush(q, (0, 1)) # 1번 헛간에서 출발
    distance = [INF]*(n+1)
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt, ndist in graph[now]:
            cost = ndist+dist
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    print(distance[n])
solution()