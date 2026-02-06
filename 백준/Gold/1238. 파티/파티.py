# 역방향 그래프 ver.
import sys, heapq
input = sys.stdin.readline

# 입력 받기
n, m, x = map(int, input().split())  # n: 학생 수, m: 도로 수, x: 파티 마을
graph = [[] for _ in range(n+1)]         # 정방향 그래프 (x → 다른 마을)
reverse_graph = [[] for _ in range(n+1)] # 역방향 그래프 (다른 마을 → x)

# 그래프 구성
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))         # 정방향
    reverse_graph[v].append((u, w)) # 역방향

# 다익스트라 함수 (시작점에서 각 노드까지의 최단거리 구함)
def dijkstra(start, graph):
    distance = [int(1e9)] * (n+1)
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
    return distance

# X → 모든 마을 (정방향)
go = dijkstra(x, graph) 
# 모든 마을 → X (역방향, 즉 X로 오는 비용)
back = dijkstra(x, reverse_graph)

# 왕복 시간 중 가장 긴 값 찾기
max_total = 0
for i in range(1, n+1):
    total = go[i] + back[i]
    max_total = max(max_total, total)

print(max_total)