import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():
    n, m = map(int, input().split()) # 사람 수, 친구 관계 수
    friend = [[] for _ in range(n)]
    visited = [False]*(n)
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a].append(b)
        friend[b].append(a)

    def dfs(a, depth):
        if depth >= 5:
            print(1)
            sys.exit()
        
        visited[a] = True
        for b in friend[a]:
            if not visited[b]:
                dfs(b, depth+1)
        visited[a]=False

    for i in range(n):
        dfs(i, 1)
    print(0)
solution()