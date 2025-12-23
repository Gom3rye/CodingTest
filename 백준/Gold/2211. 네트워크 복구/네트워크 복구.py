import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #컴퓨터 <=1000, #회선
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c)) # 양방향
        graph[b].append((a, c))
    INF = float('inf')
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance = [INF]*(n+1)
        distance[start] = 0
        parents = [-1]*(n+1)
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, ndist in graph[now]:
                cost = ndist+dist
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    parents[nxt] = now
                    heapq.heappush(q, (cost, nxt))
        return parents
    
    parents = dijkstra(1)
    print(len(parents[2:]))
    for i in range(2, n+1):
        print(i, parents[i])
solution()