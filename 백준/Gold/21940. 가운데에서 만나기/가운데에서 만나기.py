import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    INF = float('inf')
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a][b] = t
    for i in range(n+1):
        graph[i][i] = 0
    
    k = int(input())
    cities = list(map(int, input().split()))
    def floyd():
        for k in range(1, n+1):
            for a in range(1, n+1):
                for b in range(1, n+1):
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    floyd()
    dist = []
    for x in range(1, n+1):
        flag = True # 친구<->x<->친구 가 가능해야 하기 때문에 flag 필요
        longest_distance = 0
        for ppl in cities:
            roundtrip = graph[ppl][x]+graph[x][ppl]
            if graph[ppl][x] == INF or graph[x][ppl] == INF:
                flag = False
                break
            longest_distance = max(longest_distance, roundtrip)
        if flag:
            dist.append(longest_distance)
    min_d = min(dist)
    answer = []
    for idx, x in enumerate(dist):
        if x == min_d:
            answer.append(idx+1)
    print(*answer) 
solution()