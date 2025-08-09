import sys, heapq
input = sys.stdin.readline
def solution():
    # 한 집에서 다른 집으로 모두 왕래할 수 있어야 한다.(MST)
    def prim(start):
        visited = [False]*m
        mst_cost = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            # 이미 방문한(MST에 포함된) 집이면 건너뜀
            if visited[now]:
                continue
            # MST에 포함
            visited[now] = True
            mst_cost += dist
            # 현재 집과 연결된 모든 길을 우선 순위 큐에 추가
            for nxt, ndist in graph[now]:
                if not visited[nxt]:
                    heapq.heappush(q, (ndist, nxt))
        return mst_cost
    while True:
        m, n = map(int, input().split()) # 집의 수, 길의 수
        if m == 0 and n == 0:
            break
        graph = [[] for _ in range(m)]
        total_cost = 0
        for _ in range(n):
            x, y, z = map(int, input().split())
            graph[x].append((y, z))
            graph[y].append((x, z))
            total_cost += z
        print(total_cost-prim(0))
solution()
