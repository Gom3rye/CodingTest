import sys
input = sys.stdin.readline
import heapq
def solution():
    n = int(input()) # 땅 후보의 개수
    a, b, c = map(int, input().split()) # 친구 a, b, c
    m = int(input()) # 도로
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        d, e, l = map(int, input().split())
        graph[d].append((e, l))
        graph[e].append((d, l)) # 양방향 가능하다고 했으니까
    INF = float('inf')
    def dijkstra(start):
        q = []
        distance = [INF]*(n+1)
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, nd in graph[now]:
                cost = dist + nd
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
        return distance[1:]
    home = [[]]
    for f in [a, b, c]:
        d = dijkstra(f)
        home.append(d)
    # print(home)
    farthest = -1
    for h in range(n):
        min_result = INF
        for f in range(1, 4):
            if home[f][h] < min_result:
                min_result = home[f][h]
        if min_result > farthest:
            farthest = min_result
            final_h = h+1
    print(final_h)
solution()