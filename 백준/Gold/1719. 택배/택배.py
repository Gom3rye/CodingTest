import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 집하장의 개수, 경로의 개수
    INF = int(1e9)
    graph = [[INF]*n for _ in range(n)]
    # delivery[i][j]는 i에서 j로 갈 때, 가장 먼저 가야 할 노드 번호(1-based)
    delivery = [['-']*n for _ in range(n)] # 자기 자신은 -
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
        delivery[a-1][b-1] = b # a->b로 가는 첫 노드는 b
        delivery[b-1][a-1] = a # b->a로 가는 첫 노드는 a
    for i in range(n):
        graph[i][i] = 0
    def floyd():
        for k in range(n):
            for a in range(n):
                if graph[a][k] == INF:
                    continue
                for b in range(n):
                    if graph[k][b] != INF:
                        if graph[a][b] > graph[a][k] + graph[k][b]:
                            graph[a][b] = graph[a][k] + graph[k][b]
                            delivery[a][b] = delivery[a][k]
    floyd()
    for i in range(n):
        print(*delivery[i])
solution()