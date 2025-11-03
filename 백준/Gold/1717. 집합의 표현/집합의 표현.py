import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    parents = list(range(n+1))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        pa = find(a)
        pb = find(b)
        if pa < pb:
            parents[pb] = pa
        else:
            parents[pa] = pb
    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0: # 합집합인 경우
            union(a, b)
        else: # op == 1
            if find(a) != find(b):
                print("NO")
            else:
                print('YES')
solution()