import sys
input = sys.stdin.readline
import heapq
def solution():
    n = int(input()) # 도시의 개수
    m = int(input()) # 버스의 개수
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    s, d = map(int, input().split())
    INF = float('inf')
    def dijkstra(start):
        q = []
        distance = [INF]*(n+1)
        distance[start] = 0
        prev = [-1]*(n+1) # 경로 담아낼 역추적을 위한 배열
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for nxt, nd in graph[now]:
                cost = dist + nd
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    prev[nxt] = now
                    heapq.heappush(q, (cost, nxt))
        return distance[d], prev
    min_d, prev = dijkstra(s)
    print(min_d)
    prev.append(s)
    # print(len(prev)) 여기에는 최단 경로가 될 수 있는 모든 노드들이 모여있으므로 정답x
    temp = d
    track = []
    while temp != -1:
        track.append(temp)
        temp = prev[temp]
    print(len(track))
    print(*track[::-1])
solution()