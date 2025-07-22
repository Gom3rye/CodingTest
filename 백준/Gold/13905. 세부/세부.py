import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 집, 다리의 수
    s, e = map(int, input().split()) # 숭이의 출발 위치, 혜빈이의 위치(도착 위치)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def dijkstra(limit, s):
        q = []
        heapq.heappush(q, (-limit, s)) # -를 붙여서 max_heap 만들기
        max_limit = [0]*(n+1)
        max_limit[s] = limit
        while q:
            limit, now = heapq.heappop(q)
            limit = -limit # -를 붙여서 넣어줬으니까 빼고 난 후는 원상 복구

            if now == e:
                print(limit)
                return
            
            if limit < max_limit[now]: # 현재 max_limit 값보다 limit이 작으면 갱신할 필요 없으니까 pass 
                continue

            for nxt, next_limit in graph[now]:
                affordable = min(limit, next_limit)
                if affordable > max_limit[nxt]:
                    max_limit[nxt] = affordable
                    heapq.heappush(q, (-affordable, nxt))

        print(0) # s -> e 까지의 경로가 없다면 아무것도 가져갈 수 없으니 0 출력
        return
    dijkstra(1000001, s)
solution()