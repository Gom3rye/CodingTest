import sys, heapq
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # #도시 <=10000, #도로 <=50000, #포장 도로 <=20
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c)) # 양방향
    # k개 이하의 도로를 0으로 지나면서 1->n으로 도착할 수 있는 최소 시간
    # 50000 C 20은 너무 큼 -> dp이용해서 상태관리하자 dp[node][k]: k번을 포장해서 node까지 온 최단시간
    INF = float('inf')
    dp = [[INF]*(k+1) for _ in range(n+1)]
    q = []
    dp[1][0] = 0
    heapq.heappush(q, (0, 1, 0)) # dist, now, cnt(k)
    while q:
        dist, now, cnt = heapq.heappop(q)
        if dist > dp[now][cnt]:
            continue
        for nxt, ndist in graph[now]:
            # 포장하지 않는 경우
            cost = ndist+dist
            if cost < dp[nxt][cnt]:
                dp[nxt][cnt] = cost
                heapq.heappush(q, (cost, nxt, cnt))
            # 지금 노드-nxt와의 도로를 포장하는 경우
            cost = dist
            if cnt < k and cost < dp[nxt][cnt+1]:
                dp[nxt][cnt+1] = cost
                heapq.heappush(q, (cost, nxt, cnt+1))            
    print(min(dp[n]))
solution()