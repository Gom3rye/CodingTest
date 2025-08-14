import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(m):
        pre, nxt = map(int, input().split())
        graph[pre].append(nxt)
        indegree[nxt] += 1
    period = [1]*(n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i) # 선수과목 없는 것들 먼저 듣기 위해 큐에 넣기
    while q:
        pre = q.popleft()
        for nxt in graph[pre]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                period[nxt] = period[pre]+1
                q.append(nxt)
    print(*period[1:])
solution()