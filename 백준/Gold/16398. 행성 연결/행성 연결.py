import sys
input = sys.stdin.readline
def solution():
    # 모든 행성을 연결하면서 플로우 관리 비용 최소화 -> MST
    n = int(input()) # 행성의 수
    board = [list(map(int, input().split())) for _ in range(n)]
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            edges.append((board[i][j], i, j))
    edges.sort()
    parents = list(range(n+1))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
    min_cost = 0
    for cost, i, j in edges:
        if find(i) != find(j):
            union(i, j)
            min_cost += cost
    print(min_cost)
solution()
