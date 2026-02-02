import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split()) # 정점, 간선
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향
v1, v2 = map(int, input().split()) # 반드시 지나야 하는 정점
def dijkstra(start):
    distance=[INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance # start에서 시작한 최단 거리 배열 반환
# 1 -> v1 -> v2 -> n까지의 최단 거리
distance_from_1 = dijkstra(1)
distance_from_v1 = dijkstra(v1)
distance_from_v2 = dijkstra(v2)

v1_to_v2 = distance_from_1[v1] + distance_from_v1[v2] + distance_from_v2[n]
v2_to_v1 = distance_from_1[v2] + distance_from_v2[v1] + distance_from_v1[n]
# 세 경로 중 하나라도 int(1e9)이면 print(-1)을 해야 한다. -> 결과 값이 int(1e9) 이상인지 확인!
result = min(v1_to_v2, v2_to_v1)
print(result if result < INF else -1)