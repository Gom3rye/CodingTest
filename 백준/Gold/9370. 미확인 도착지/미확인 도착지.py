import sys, heapq
input = sys.stdin.readline
def solution():
    # s에서 dest로 가는 최단 경로가 g–h 도로를 반드시 포함하는 dest만 오른차순으로 출력
    T = int(input()) # 테스트 케이스
    for _ in range(T):
        n, m, t = map(int, input().split()) # 교차료 <=2000, 도로 <=50000, 목적지 후보 <=100
        s, g, h = map(int, input().split()) # 출발지, 교차료
        graph = [[] for _ in range(n+1)]
        gh_dist = 0
        for _ in range(m):
            a, b, d = map(int, input().split())
            if (a == g and b == h) or (a == h and b == g):
                gh_dist = d
            graph[a].append((b, d))
            graph[b].append((a, d))
        possible_dest = list(int(input()) for _ in range(t)) # 목적지 후보들
        INF = float('inf')
        def dijkstra(start):
            distance = [INF]*(n+1) # 1based index
            distance[start] = 0
            q = []
            heapq.heappush(q, (0, start))
            while q:
                dist, now = heapq.heappop(q)
                if dist > distance[now]:
                    continue
                
                for nxt, ndist in graph[now]:
                    cost = dist+ndist
                    if cost < distance[nxt]:
                        distance[nxt] = cost
                        heapq.heappush(q, (cost, nxt))
            return distance
        # g-h를 지나며 최단 거리로 목적지에 도착했는지 알기 위해서는 최단거리(s-목적지) == 최단거리(s-g-h-목적지 or s-h-g-목적지) 여야 한다.
        from_start = dijkstra(s)
        from_g = dijkstra(g)
        from_h = dijkstra(h)

        answer = []
        for dest in possible_dest:
            if from_start[dest] >= INF:
                continue
            # s-g-h-dest
            if from_start[dest] == from_start[g]+gh_dist+from_h[dest]:
                answer.append(dest)
            # s-h-g-dest
            elif from_start[dest] == from_start[h]+gh_dist+from_g[dest]:
                answer.append(dest)
        print(*sorted(answer))
    
solution()