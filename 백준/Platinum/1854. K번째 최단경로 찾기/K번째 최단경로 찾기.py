import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def solution():
    n, m, k = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # dist[i]: 1번에서 i번 도시까지의 k개의 최단 경로를 '최대 힙'으로 저장
    # (실제로는 최소 힙에 음수로 저장하여 흉내)
    dist = [[] for _ in range(n + 1)]
    
    # 우선순위 큐 초기화: (비용, 도시 번호)
    pq = [(0, 1)]
    # 1번 도시의 첫 최단 경로는 비용 0
    heapq.heappush(dist[1], 0)

    while pq:
        cost, current_node = heapq.heappop(pq)
        
        # 이웃 노드로 탐색 확장
        for neighbor, weight in graph[current_node]:
            new_cost = cost + weight
            
            # neighbor까지의 경로가 k개 미만이거나,
            # 새로 찾은 경로가 기존 k번째 경로보다 더 좋은 경우
            if len(dist[neighbor]) < k:
                heapq.heappush(dist[neighbor], -new_cost) # 최대 힙에 음수로 저장
                heapq.heappush(pq, (new_cost, neighbor))
            elif new_cost < -dist[neighbor][0]: # dist[neighbor][0]은 k개 중 최댓값
                heapq.heappushpop(dist[neighbor], -new_cost)
                heapq.heappush(pq, (new_cost, neighbor))

    # 결과 출력
    for i in range(1, n + 1):
        if len(dist[i]) == k:
            # 최대 힙의 루트는 가장 작은 음수 값 -> 절댓값이 가장 큰 값 -> k번째 최단 경로
            print(-dist[i][0])
        else:
            print(-1)

solution()