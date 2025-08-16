import sys
from collections import deque
input = sys.stdin.readline
def solution():
    a, b, n, m = map(int, input().split()) # 스카이 콩콩의 힘a,b , 동규와 주미의 위치
    q = deque([(n, 0)])
    visited = [False]*100001
    visited[n] = True
    while q:
        now, time = q.popleft()
        if now == m:
            print(time)
            return
        
        for nxt in [now-1, now+1, now+a, now+b, now-a, now-b, now*a, now*b]:
            if 0<=nxt<=100000 and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, time+1))

solution()