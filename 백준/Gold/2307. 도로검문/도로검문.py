import sys, heapq
from math import log2
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m = map(int, input().split()) # #지점 <=1000, #도로 <=5000
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        graph[b].append((a, t)) # 양방향
    
    # 최단 경로를 구성하는 도로들을 하나씩 막아보며 max_delay 계산
    def dijkstra(start, ban=(a, b)):
        q = []
        heapq.heappush(q, (0, start))
        distance = [INF]*(n+1)
        distance[start] = 0
        prev = [-1]*(n+1)
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, ndist in graph[now]:
                if (now, nxt) == ban or (nxt, now) == ban:
                    continue
                cost = ndist+dist
                if cost < distance[nxt]:
                    prev[nxt] = now
                    distance[nxt] = cost
                    heapq.heappush(q, (cost ,nxt))
        return distance[-1], prev
    original, prev = dijkstra(1, ban=False)
    # 최단 경로를 이루는 도로 역추적
    path = []
    temp = n
    while prev[temp] != -1:
        path.append((prev[temp], temp))
        temp = prev[temp]
    
    max_delay = -1
    for a, b in path:
        dist, _ = dijkstra(1, ban=(a, b))
        if dist == INF: # 지연 시간을 무한대로 할 수 있으면 -1출력
            print(-1)
            return
        max_delay = max(max_delay, dist-original)
    print(max_delay)
solution()