import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #구슬 <=99(홀수), #저울에 올려 본 쌍 <=n*(n-1)/2
    # 중간이 될 수 없는 구슬의 개수 구하기 (중간: (N+1)/2번째))
    mid = (n+1)//2
    lighter = [[] for _ in range(n+1)]
    heavier = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split()) # a > b무거움
        lighter[a].append(b) # a보다 b가 더 가볍다.
        heavier[b].append(a)
    # print(lighter)
    # print()
    # print(heavier)
    def bfs(graph, start):
        q = deque()
        q.append(start)
        visited = [False]*(n+1)
        visited[start] = True
        cnt = 0
        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    cnt += 1
        return cnt
    answer = 0
    for i in range(1, n+1):
        light = bfs(lighter, i) # i보다 가벼운 수
        heavy = bfs(heavier, i) # i보다 무거운 수
        if light >= mid or heavy >= mid:
            answer += 1

    print(answer)
solution()