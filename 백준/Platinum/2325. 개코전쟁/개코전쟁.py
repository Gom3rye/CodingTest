import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z)) # 양방향
        graph[y].append((x, z))
    INF = float('inf')
    def dijkstra(start, v1, v2, ban):
        q = []
        distance = [INF]*(n+1)
        distance[start] = 0
        prev = [0]*(n+1) # 최단 거리를 이루는 간선 중 하나를 파괴해야 함 -> 역추적
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, ndist in graph[now]:
                if ban:
                    if now == v1 and nxt == v2:
                        continue
                    elif now == v2 and nxt == v1:
                        continue # 양방향 도로 막기
                cost = dist+ndist
                if cost < distance[nxt]:
                    prev[nxt] = now
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
                    
        return distance[-1], prev
    _, prev = dijkstra(1, -1, -1, False)
    # 경로 추적
    path = []
    temp = n
    while prev[temp] != 0:
        path.append((prev[temp], temp))
        temp = prev[temp]
    path.reverse()
    # 이 경로 상의 간선을 하나씩 막으면서 최장 최단거리 구하기
    longest_time = 0
    for v1, v2 in path:
        dist, _ = dijkstra(1, v1, v2, True)
        longest_time = max(longest_time, dist)
    print(longest_time)

solution()