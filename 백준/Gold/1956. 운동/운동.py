import sys
input = sys.stdin.readline
def solution():
    v, e = map(int, input().split()) # 노드 <400, 간선 <160000
    INF = float('inf')
    graph = [[INF]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    for i in range(1, v+1):
        graph[i][i] = 0
    def floyd():
        for k in range(1, v+1):
            for a in range(1, v+1):
                for b in range(1, v+1):
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    floyd()
    min_cost = INF
    for i in range(1, v+1):
        for j in range(1, v+1):
            if i == j:
                continue
            if graph[i][j] != INF and graph[j][i] != INF:
                min_cost = min(min_cost, graph[i][j]+graph[j][i])
    
    print(min_cost if min_cost != INF else -1)
            
solution()