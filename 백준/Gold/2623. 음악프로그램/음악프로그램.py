import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 가수번호 <=1000, 보조pd가 정한 순서 <=100
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        order = list(map(int, input().split()))
        cnt = order[0]
        for singer in range(1, order[0]):
            prev, nxt = order[singer], order[singer+1]
            graph[prev].append(nxt)
            indegree[nxt] += 1
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    answer = []
    while q:
        now = q.popleft()
        answer.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    if len(answer) == n:
        print(*answer, sep='\n')
    else:
        print(0)
            
solution()