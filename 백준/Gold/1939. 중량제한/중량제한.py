import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
max_w = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_w = max(max_w, c)

start, end = map(int, input().split())


def can_go(limit):
    visited = [False]*(N+1)
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()

        for nxt, w in graph[now]:
            if not visited[nxt] and w >= limit:
                visited[nxt] = True
                q.append(nxt)

    return visited[end]


low, high = 1, max_w
answer = 0

while low <= high:
    mid = (low + high) // 2

    if can_go(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
