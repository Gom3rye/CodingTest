import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, a, b = map(int, input().split()) # 강아지, 닫힌구간, a,b 생성마법
    visited = [False]*(n+1)
    for i in range(m):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            visited[j] = True
    q = deque([(0, 0)])
    visited[0] = True
    while q:
        now, count = q.popleft()
        for nxt in [now+a, now+b]:
            if not (0<=nxt<=n):
                continue
            if nxt == n:
                print(count+1)
                return
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, count+1))
    print(-1)
solution()