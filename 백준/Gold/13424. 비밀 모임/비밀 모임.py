import sys
input = sys.stdin.readline
import heapq
def solution():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))
            
        k = int(input()) # 친구 수
        k_list = list(map(int, input().split()))
        INF = int(1e9)
        # 이동 거리 총합이 최소가 되도록 하는 모임 장소의 방 번호 출력
        def dijkstra(k1):
            q = []
            heapq.heappush(q, (0, k1)) # cost, start_node
            distance = [INF] * (n+1)
            distance[k1] = 0
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
        
        room_d = [0]*(n+1)
        result = 0
        for i in k_list:
            dist = dijkstra(i)
            min_d = INF # 친구마다 최단 거리는 다를 수 있으니까
            for r in range(1, n+1):
                room_d[r] += dist[r]
                if room_d[r] < min_d:
                    min_d = room_d[r]
                    result = r
        print(result)
solution()