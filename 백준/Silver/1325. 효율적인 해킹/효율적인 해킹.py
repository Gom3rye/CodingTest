import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #컴퓨터 <=10000, #관계 <=100,000
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a) # a->b신뢰, b를 해킹하면 a도 해킹할 수 있다.

    def bfs(now):
        q = deque([now])
        visited = [False]*(n+1)
        visited[i] = True
        cnt = 1
        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    q.append(nxt)
        return cnt

    answer = []
    max_cnt = 0
    for i in range(1, n+1):
        cnt = bfs(i)
        if max_cnt < cnt:
            max_cnt = cnt
            answer = [i]
        elif max_cnt == cnt:
            answer.append(i)
    print(*answer)
solution()