import heapq
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    
    distance = [INF] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    queue = []
    heapq.heappush(queue, (0, 1)) # 
    distance[1] = 0
    while queue:
        w, v1 = heapq.heappop(queue)
        
        for v2 in graph[v1]:
            cost = w + 1
            if cost < distance[v2]:
                distance[v2] = cost
                heapq.heappush(queue, (cost, v2))
    
    answer_node = 0
    answer_distance = 0
    ansewr_max_num = 0
    for i in range(1, N+1):
        if distance[i] > answer_distance:
            answer_node = i
            answer_distance = distance[i]
            ansewr_max_num = 1
        elif distance[i] == answer_distance:
            ansewr_max_num += 1
            
    print(answer_node, answer_distance, ansewr_max_num)

if __name__ == "__main__":
    solution()