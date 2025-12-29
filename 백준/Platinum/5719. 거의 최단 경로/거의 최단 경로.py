import sys, heapq
from collections import deque
input = sys.stdin.readline
def solution():
    # 거의 최단 경로의 길이 출력, if nothing-> -1출력
    while True:
        n, m = map(int, input().split()) # #장소 <=500, #도로 <=10^4
        if n == m == 0:
            break
        s, d = map(int, input().split()) # 시작점, 도착점
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            graph[u].append((v, p))
        # 최단경로가 아닌 도로 중에서 골라야 하니까 최단 경로를 구성하는 도로의 정보를 알기 위해 역추적 필요
        # 근데 prev[nxt] = now가 아니라 now가 여러 개 일 수 있으니까 list로 관리하기
        blocked = [[False]*n for _ in range(n)]
        INF = float('inf')
        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            distance = [INF]*n
            distance[start] = 0
            prev = [[] for _ in range(n)]
            while q:
                dist, now = heapq.heappop(q)
                if dist > distance[now]:
                    continue
                for nxt, ndist in graph[now]:
                    if blocked[now][nxt]:
                        continue
                    cost = ndist+dist
                    if cost < distance[nxt]:
                        distance[nxt] = cost
                        prev[nxt] = [now] # now <- nxt 경로 세팅
                        heapq.heappush(q, (cost, nxt))
                    elif cost == distance[nxt]:
                        prev[nxt].append(now)
            return prev, distance[d]
        prev, _ = dijkstra(s)
        # 하나씩 돌아가며 blocked 표시하기 by 무한대값 주면서
        q = deque([d])
        while q:
            now = q.popleft()
            for pre in prev[now]:
                if not blocked[pre][now]:
                    blocked[pre][now] = True
                    q.append(pre)
        _, almost_shortest = dijkstra(s)
        print(almost_shortest if almost_shortest != INF else -1)
solution()