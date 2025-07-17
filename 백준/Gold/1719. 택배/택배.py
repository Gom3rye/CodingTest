import sys
input = sys.stdin.readline
import heapq
def solution():
    n, m = map(int, input().split()) # 집하장의 개수, 경로의 개수
    INF = int(1e9)
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
        
    def dijkstra(start):
        distance = [INF]*n
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        delivery = ['-']*n # 최단 경로 첫 노드 저장, 자기 자신은 '-'
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, nd in graph[now]:
                cost = dist + nd
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))

                    # 첫 번째 거쳐야 할 노드 갱신
                    if now == start:
                        delivery[nxt] = nxt+1 # 1-based index
                    else:
                        delivery[nxt] = delivery[now]
        return delivery
    
    for i in range(n):
        print(*dijkstra(i))

solution()