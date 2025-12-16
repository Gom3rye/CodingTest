import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    t = int(input()) # <=100
    for _ in range(t):
        n, m = map(int, input().split()) # 섬의 수 <=1000, 다리의 수
        # 다리가 하나밖에 없는 섬에서 루팡 있다.
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))
        # 위험성 있는 섬 구하기
        possible = set()
        for i in range(2, n+1): # 1번섬 제외
            if len(graph[i]) == 1:
                possible.add(i)
        INF = float('inf')
        def dfs(now, parent):
            if now in possible:
                return INF
            cost = 0
            for u, w in graph[now]:
                if u == parent:
                    continue

                cost += min(dfs(u, now), w)
            return cost
        print(dfs(1, -1))

solution()