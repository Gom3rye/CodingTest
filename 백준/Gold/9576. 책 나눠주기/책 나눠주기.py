import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[a] = b

def solution():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        parent = [i for i in range(n+2)]  # n+1까지 만들기 (범위 초과 방지)

        infos = [tuple(map(int, input().split())) for _ in range(m)]
        infos.sort(key=lambda x: x[1])

        cnt = 0
        for a, b in infos:
            available = find(parent, a)
            if available <= b:
                union(parent, available, available + 1)
                cnt += 1
        print(cnt)

solution()