import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, a, b = map(int, input().split()) # 강아지, 닫힌구간, a,b 생성마법
    spots = [list(map(int, input().split())) for _ in range(m)]
    q = deque([(0, 0)])
    visited = [False]*(n+1)
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
                for i in range(m):
                    if spots[i][0] <= nxt <= spots[i][1]:
                        break
                else:
                    visited[nxt] = True
                    q.append((nxt, count+1))
    print(-1)
solution()