import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 인접 리스트 오름차순 정렬
    for neighbors in graph:
        neighbors.sort()

    visited = [0] * (N + 1)  # 방문 순서 기록
    order = 1

    def dfs(node):
        nonlocal order
        visited[node] = order
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                order += 1
                dfs(neighbor)

    dfs(R)

    for i in range(1, N + 1):
        print(visited[i])
solution()