import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

N = int(input())

# 트리 구성
tree = [[] for _ in range(N + 1)]
info = [None] * (N + 1)

for i in range(2, N + 1):
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    info[i] = (t, a)
    tree[p].append(i)

def dfs(u):
    sheep = 0

    # 자식에서 올라온 양 합치기
    for v in tree[u]:
        sheep += dfs(v)

    # 현재 섬 처리
    if u != 1:
        t, a = info[u]
        if t == 'S':
            sheep += a
        else:  # 'W'
            sheep -= a
            if sheep < 0:
                sheep = 0

    return sheep

print(dfs(1))