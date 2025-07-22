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
    
    result = 0
    def dijkstra(min_affordable, s):
        nonlocal result
        q = []
        heapq.heappush(q, (min_affordable, s))
        visited = [False]*(n+1)
        while q:
            min_affordable, start = heapq.heappop(q)
            min_affordable = -min_affordable

            if start == e:
                result = max(min_affordable, result)
                return
            
            if visited[start]:
                continue
            visited[start] = True

            for next, affordable in graph[start]:
                if not visited[next]:
                    affordable = min(affordable, min_affordable)
                    heapq.heappush(q, (-affordable, next))

    dijkstra(-1000001, s)
    print(result)
solution()