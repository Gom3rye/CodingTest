import sys, heapq
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 도시, 케이블, 발전소
    graph = [[] for _ in range(n+1)]
    factory = list(map(int, input().split()))
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    def prim():
        visited = [False]*(n+1)
        q = []
        total_cost = 0
        for f in factory:
            visited[f] = True
            for nxt, ndist in graph[f]:
                heapq.heappush(q, (ndist, nxt))
        while q:
            dist, now = heapq.heappop(q)
            if visited[now]:
                continue
            visited[now] = True
            total_cost += dist
            for nxt, ndist in graph[now]:
                if not visited[nxt]:
                    heapq.heappush(q, (ndist, nxt))
        return total_cost
    print(prim())
solution()