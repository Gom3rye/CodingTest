import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    INF = float('inf')
    graph = [[INF]*n for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a-1][b-1] = t
    for i in range(n):
        graph[i][i] = 0
    
    k = int(input())
    cities = list(map(int, input().split()))
    def floyd():
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    floyd()
    dist = []
    for x in range(n): # 0based index
        flag = True # 친구<->x<->친구 가 가능해야 하기 때문에 flag 필요
        longest_distance = 0
        for ppl in cities:
            ppl -= 1 # 0based index
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
            answer.append(idx+1) # 1based index
    print(*answer) 
solution()