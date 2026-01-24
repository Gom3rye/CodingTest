import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solution():
    N = int(input())
    parent = list(map(int, input().split()))

    # 트리 만들기
    tree = [[] for _ in range(N)]
    for i in range(1, N):
        tree[parent[i]].append(i)

    def dfs(u):
        times = []
        for v in tree[u]:
            times.append(dfs(v))

        # 시간이 오래 걸리는 부하부터
        times.sort(reverse=True)

        res = 0
        for i, t in enumerate(times):
            res = max(res, t + i + 1)
        return res

    print(dfs(0))

solution()