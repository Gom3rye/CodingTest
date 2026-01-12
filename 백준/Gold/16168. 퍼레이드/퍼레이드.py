import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
def solution():
    v, e = map(int, input().split()) # #정점, #간선 <=3000
    degree = [0]*(v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) # 양방향
        degree[a] += 1
        degree[b] += 1
    # dfs로 모든 간선 도착할 수 있는지 확인
    visited = [False]*(v+1)
    visited[1] = True
    def dfs(now):
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)
    dfs(1)
    if sum(visited[1:]) != v: # 하나라도 방문하지 않은 게 있다는 거니까
        print("NO")
        return
    # 홀수인 차수가 0 또는 2개인지 확인하기
    cnt = 0
    for i in range(1, v+1):
        if degree[i]%2 == 1:
            cnt += 1
    if cnt == 0 or cnt == 2:
        print("YES")
    else:
        print("NO")
solution()