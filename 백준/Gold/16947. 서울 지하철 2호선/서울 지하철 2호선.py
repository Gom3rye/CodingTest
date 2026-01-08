import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n = int(input()) # <=3000
    graph = [[] for _ in range(n+1)]
    degree = [0]*(n+1)
    for _ in range(n):
        a, b, = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) # 무향그래프!!!-> 사이클 표시할 때 이전으로 돌아가지 않기 위해 prev도 같이 넘겨줘야 한다!
        degree[a] += 1
        degree[b] += 1
    # cycle 여부만 파악하는게 아니라 구성요소들도 구해야 하니까 degree(차수) 사용!
    q = deque()
    is_cycle = [True]*(n+1)
    for i in range(1, n+1):
        if degree[i] == 1:
            is_cycle[i] = False
            q.append(i)
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            degree[nxt] -= 1
            if degree[nxt] == 1:
                is_cycle[nxt] = False
                q.append(nxt)
    dist = [-1]*(n+1)
    q = deque()
    for i in range(1, n+1):
        if is_cycle[i]:
            dist[i] = 0
            q.append(i)
    # 위에서 구한 사이클원소들로 multi source bfs 돌려서 거리 구하기!
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                q.append(nxt)

    print(*dist[1:])
solution()