import sys, heapq
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # #도시 <=100,000, #도로 <=500,000, #면접장 <=100,000
    graph = [[] for _ in range(n+1)]
    # multi-source dijkstra) 도시 -> 면접장 => 면접장 -> 도시로 방향 바꾸기
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))
    spots = list(map(int, input().split())) # 면접장 장소
    INF = float('inf')
    def dijkstra(spots):
        q = []
        distance = [INF]*(n+1)
        for spot in spots:
            distance[spot] = 0
            heapq.heappush(q, (0, spot))
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, ndist in graph[now]:
                cost = dist+ndist
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
        max_dist = max(distance[1:])
        return max_dist, distance.index(max_dist)
    
    dist, city = dijkstra(spots)
    print(city)
    print(dist)
    
solution()