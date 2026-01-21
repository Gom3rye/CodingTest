import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #역 <=100
    # 모든 노드에서 도달 가능한 도착점 i노드가 있는지 없으면 -1출력
    graph = [[False]*(n+1) for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[b][a] = True
    for i in range(1, n+1):
        graph[i][i] = True
    def floyd():
        for k in range(1, n+1):
            for a in range(1, n+1):
                for b in range(1, n+1):
                    if graph[a][k] and graph[k][b]:
                        graph[a][b] = True
    floyd()
    for i in range(1, n+1):
        if sum(graph[i][1:]) == n:
            print(i)
            break
    else:
        print(-1)
solution()