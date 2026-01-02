import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #지역 <=100,000, 횡단보도 주기 <=700,000
    graph = [[] for _ in range(n+1)]
    for t in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, t))
        graph[b].append((a, t)) # 양방향이니까
    # 시간에 따라 변하는 주기 그래프 + 최단 시간(=경로)
    INF = float('inf')
    q = []
    heapq.heappush(q, (0, 1)) # time, now
    distance = [INF]*(n+1)
    distance[1] = 0
    while q:
        time, now = heapq.heappop(q)
        if now == n:
            print(time)
            return
        if time > distance[now]:
            continue
        for nxt, ntime in graph[now]:
            # 기다려야 하는 시간: (i-(time%m)+m)%m
            wait = (ntime-(time%m)+m)%m
            cost = time + wait + 1 # 1초는 건너는 시간
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
solution()