import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = [0] + list(map(int, input().split()))
        visited = [False] * (n+1)
        finished = [False] * (n+1)
        result = 0

        def dfs(x):
            nonlocal result
            visited[x] = True
            y = graph[x]
            if not visited[y]:
                dfs(y)
            elif not finished[y]:
                # 사이클이 형성된 경우만 카운트
                temp = y
                while temp != x:
                    result += 1
                    temp = graph[temp]
                result += 1
            finished[x] = True

        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i)

        print(n - result)
solution()