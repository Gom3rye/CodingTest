import sys, heapq
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 도시, 케이블, 발전소
    graph = [[] for _ in range(n+1)]
    factory = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    parent = list(range(n+1))

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    # 모든 발전소를 하나의 그룹으로 미리 통합 (가상의 전력원)
    for i in range(k-1):
        union_parent(factory[i], factory[i+1])

    min_cost = 0
    for dist, a, b in edges:
        # 사이클이 없을 때만
        if find_parent(a) != find_parent(b):
            # 이어주기
            union_parent(a, b)
            min_cost += dist
    print(min_cost)

solution()