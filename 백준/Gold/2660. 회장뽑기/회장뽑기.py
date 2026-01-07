import sys
from math import log2
input = sys.stdin.readline
def solution():
    n = int(input()) # #회원 <=50
    INF = float('inf')
    graph = [[INF]*(n+1) for _ in range(n+1)]
    while True:
        a, b = map(int, input().split())
        if a == b == -1:
            break
        graph[a][b] = 1
        graph[b][a] = 1
    for i in range(n+1):
        graph[i][i] = 0
    def floyd():
        for k in range(1, n+1):
            for a in range(1, n+1):
                for b in range(1, n+1):
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    floyd()
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] == INF:
                graph[i][j] = -1
    score = [INF]*(n+1)
    for i in range(1, n+1):
        score[i] = max(graph[i])
    president = []
    president_score = min(score)
    for i in range(1, n+1):
        if score[i] == president_score:
            president.append(i)
    print(president_score, len(president))
    print(*president)

solution()