import sys, heapq
from math import log2
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, p, k = map(int, input().split()) # #학생 <=1000, #케이블 <=10000, #공짜 케이블 <=n
    graph = [[] for _ in range(n+1)]
    for _ in range(p):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    # 가격이 1~1,000,000, log2(10^6)~> 20, 총 시간복잡도: log2(10**6)*10000*log2(1000))
    # -> parametric search로 최소 비용 찾으면서 dijkstra 돌리기!
    def is_valid(c):
        q = []
        heapq.heappush(q, (0, 1)) # cost, start
        distance = [INF]*(n+1)
        distance[1] = 0
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
    
            for nxt, ndist in graph[now]:
                cost = 1+dist if ndist > c else dist # 후보값인 c보다 크면 공짜쿠폰 1개 쓴거 니까 1표시, 아니면 0
                if distance[nxt] > cost:
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))

        # 1->n번까지 가는데 필요한 쿠폰(가중치 1짜리 간선)의 최소 개수가 k 이하인가?
        return distance[-1] <= k

    answer, start, end = -1, 0, 1000000 # start값 0 주의!! (공짜쿠폰만으로도 갈 수 있으니까)
    while start <= end:
        mid = (start+end)//2 # 내야 하는 최솟값
        if is_valid(mid):
            answer = mid
            end = mid-1
        else:
            start = mid+1
    print(answer)
solution()