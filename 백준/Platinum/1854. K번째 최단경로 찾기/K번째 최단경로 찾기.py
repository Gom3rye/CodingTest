import sys, heapq
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    def dijkstra(start):
        # 1->i노드까지 최단 거리를 k개 저장해놔야 하니까 2차원 배열
        distance = [[] for _ in range(n+1)] # []가 max heap의 역할을 할 것
        q = []
        heapq.heappush(q, (0, start))
        heapq.heappush(distance[start], 0)
        while q:
            dist, now = heapq.heappop(q)
            for nxt, ndist in graph[now]:
                cost = dist+ndist
                if len(distance[nxt]) < k:
                    heapq.heappush(distance[nxt], -cost)
                    heapq.heappush(q, (cost, nxt))
                elif cost < -distance[nxt][0]:
                    # distance[nxt] 힙에 -cost를 추가하고 가장 작은 원소를 제거한다.
                    heapq.heappushpop(distance[nxt], -cost)
                    heapq.heappush(q, (cost, nxt))

        return distance
    dist = dijkstra(1)
    for i in range(1, n+1):
        # i번 도시까지 k개의 경로가 있다면 마지막 값이 k번째 최단 경로
        if len(dist[i]) == k:
            print(-dist[i][0])
        else:
            print(-1)
solution()