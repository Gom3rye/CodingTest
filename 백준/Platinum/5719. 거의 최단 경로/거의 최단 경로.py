import sys, heapq
from collections import deque
input = sys.stdin.readline
def solution():
    while True:
        n, m = map(int, input().split()) # #장소 <=500, #도로 <=10,000
        if n == m == 0:
            break
        s, d = map(int, input().split()) # 시작점, 도착점
        graph = [[] for _ in range(n)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
        INF = float('inf')
        # 최단 경로에 포함되지 않는 도로로만 이루어진 최단 경로 찾기
        blocked = [[False]*n for _ in range(n)]
        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            distance = [INF]*n
            distance[start] = 0
            prev = [[] for _ in range(n)] # 경로 역추적을 위한 배열
            while q:
                dist, now = heapq.heappop(q)
                if dist > distance[now]:
                    continue

                for nxt, ndist in graph[now]:
                    if blocked[now][nxt]: # 최단 경로면 빼기 위해
                        continue
                    cost = dist+ndist
                    if cost < distance[nxt]:
                        distance[nxt] = cost
                        prev[nxt] = [now]
                        heapq.heappush(q, (cost, nxt))
                    elif cost == distance[nxt]:
                        prev[nxt].append((now))
            return prev, distance[d]
        
        prev, _ = dijkstra(s)

        # 최단 경로가 여러 개일 수 있으므로 bfs로 역추적
        def bfs(prev, destination):
            q = deque()
            q.append(destination)
            while q:
                dest = q.popleft()
                for pre in prev[dest]:
                    if not blocked[pre][dest]:
                        blocked[pre][dest] = True
                        q.append(pre)
        bfs(prev, d)
        # block 표시 다 했으니 다시 최단 경로 구하기
        _, almost_shortest = dijkstra(s)
        print(almost_shortest if almost_shortest != INF else -1)
         
solution()