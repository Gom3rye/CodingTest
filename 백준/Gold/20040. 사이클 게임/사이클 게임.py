import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 점, 차례 수
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    parent = list(range(n))
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
    times = 0
    for a, b in edges:
        times += 1
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
        else:
            print(times)
            return
    print(0)
solution()