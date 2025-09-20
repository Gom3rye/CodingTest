import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드-워셜 알고리즘
for k in range(n):
    for i in range(n):
        if not graph[i][k]:
            continue
        for j in range(n):
            # graph[i][k]와 graph[k][j]가 1이라면 i->k->j 경로가 존재한다는 뜻
            if graph[k][j]:
                graph[i][j] = 1

# 출력
for row in graph:
    print(*row)