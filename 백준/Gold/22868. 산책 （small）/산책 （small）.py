import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        graph[i].sort()
    s, e = map(int, input().split())
    prev = [-1]*(n+1)
    def go(start):
        q = deque([(start, 0)])
        visited = [False]*(n+1)
        visited[start] = True
        while q:
            now, dist = q.popleft()
            if now == e:
                return dist, prev
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    prev[nxt] = now
                    q.append((nxt, dist+1))

    dist, prev = go(s)
    block = set()
    temp = e
    while temp != -1:
        block.add(temp)
        temp = prev[temp]
    block -= {s}
    def back(start, dist):
        q = deque([(start, dist)])
        visited = [False]*(n+1)
        visited[start] = True
        while q:
            now, dist = q.popleft()
            if now == s:
                return dist
            for nxt in graph[now]:
                if not visited[nxt] and nxt not in block:
                    visited[nxt] = True
                    q.append((nxt, dist+1))
    print(back(e, dist))
solution()