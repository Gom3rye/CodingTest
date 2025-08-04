import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    # 시작 노드는 1, 늑대는 d/2 -> d*2 -> d/2 반복
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        # 오솔길은 어떤 방향으로든 지나갈 수 있으며 -> 양방향
        graph[b].append((a, d))
    INF = float('inf')
    fdistance = [INF]*(n+1) # 여우가 간 거리
    wdistance = [[INF, INF] for _ in range(n+1)] # 늑대가 간 거리(상태 분리가 필요하므로 2차원으로 생성)
    # wdistance[i][0]: i번 노드를 짝수 깊이에 도착한 거리, wdistance[i][1]: i번 노드를 홀수 깊이에 도착한 거리
    def fdijkstra(start):
        fdistance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)

            if dist > fdistance[now]:
                continue
            for nxt, ndist in graph[now]:
                cost = dist + ndist
                if cost < fdistance[nxt]:
                    fdistance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
        return fdistance[1:]
    def wdijkstra(start):
        wdistance[start][0] = 0
        q = []
        heapq.heappush(q, (0, start, 0))
        while q:
            dist, now, depth = heapq.heappop(q)
            parity = depth%2 # now 노드의 상태
            if dist > wdistance[now][parity]:
                continue
            for nxt, ndist in graph[now]:
                if parity == 0: # 짝수이면 2배 빨라지기
                    cost = dist+(ndist/2)
                else: # 홀수이면 2배 느려지기
                    cost = dist+(ndist*2)
                nxt_parity = (depth+1)%2 # 이동 후의 홀짝
                if cost < wdistance[nxt][nxt_parity]: # 이동 후의 상태로 갱신해야 함
                    wdistance[nxt][nxt_parity] = cost
                    heapq.heappush(q, (cost, nxt, depth+1))
        return [min(wdistance[i]) for i in range(1, n+1)]
    fdistance = fdijkstra(1)
    wdistance = wdijkstra(1)
    count = 0
    # print(f"fox: {fdistance}")
    # print(f"wolf: {wdistance}")
    for i in range(1, n): # i는 여우가 늑대보다 먼저 도락할 수 있는 노드
        if fdistance[i] < wdistance[i]:
            count += 1
    print(count)
solution()