import sys
import heapq
input = sys.stdin.readline

def get_spanning_tree_uphill_count(n, graph, find_max):
    # n+1개의 건물(0~n)이 모두 연결되었는지 확인하기 위한 visited 배열
    visited = [False] * (n + 1)
    
    # 우선순위 큐(heap)와 시작점 설정
    heap = []
    # 입구(0번)와 연결된 모든 도로를 힙에 추가
    for neighbor, cost in graph[0]:
        if find_max:
            heapq.heappush(heap, (-cost, 0, neighbor)) # Max Heap (비용에 음수)
        else:
            heapq.heappush(heap, (cost, 0, neighbor)) # Min Heap (일반)

    visited[0] = True
    uphill_count = 0
    edge_count = 0
    
    while heap and edge_count < n:
        cost, start_node, end_node = heapq.heappop(heap)
        
        if visited[end_node]:
            continue
            
        visited[end_node] = True
        edge_count += 1
        
        # 비용이 음수였다면 원래 값으로 되돌림 (Max Heap의 경우)
        original_cost = -cost if find_max else cost
        if original_cost == 1: # 오르막길인 경우
            uphill_count += 1
            
        # 새로 연결된 노드의 이웃들을 힙에 추가
        for next_neighbor, next_cost in graph[end_node]:
            if not visited[next_neighbor]:
                if find_max:
                    heapq.heappush(heap, (-next_cost, end_node, next_neighbor))
                else:
                    heapq.heappush(heap, (next_cost, end_node, next_neighbor))

    return uphill_count

def solution():
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]
    for _ in range(M + 1):
        A, B, C = map(int, input().split())
        cost = 1 - C # 오르막길(0) -> 1, 내리막길(1) -> 0
        graph[A].append((B, cost))
        graph[B].append((A, cost))

    # 최적 경로의 오르막길 개수 (find_max=False)
    k_min = get_spanning_tree_uphill_count(N, graph, False)
    
    # 최악 경로의 오르막길 개수 (find_max=True)
    k_max = get_spanning_tree_uphill_count(N, graph, True)
    
    print(k_max**2 - k_min**2)

solution()