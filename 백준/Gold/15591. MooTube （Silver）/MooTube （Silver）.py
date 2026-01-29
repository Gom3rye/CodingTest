import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, q = map(int, input().split()) # #동영상 <=5000, q <=5000
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    for _ in range(q):
        k, v = map(int, input().split()) # <=1,000,000,000, <=n
        visited = [False]*(n+1)
        visited[v] = True
        q = deque([v])
        cnt = 0
        while q:
            now = q.popleft()
            for nxt, score in graph[now]:
                if not visited[nxt] and score >= k:
                    cnt += 1
                    visited[nxt] = True
                    q.append(nxt)
        print(cnt)      
solution()