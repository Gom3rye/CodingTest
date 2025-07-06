import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, k = map(int, input().split()) # n: 수빈 위치, k: 동생 위치
    def bfs(n):
        q = deque([(n, 0)]) # (현재 위치, 시간)
        visited = [False]*100001
        visited[n]= True
        while q:
            now, time = q.popleft()
            if now == k:
                return time
            for next in [now*2, now-1, now+1]:
                if 0<= next <= 100000 and not visited[next]:
                    visited[next] = True
                    q.append((next, time+1))
    print(bfs(n))

solution()