import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, banned, n, graph):
    q = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    size = 1 # start 한개 가지고 있음(자기자신)
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            # 막힌 간선인지 체크
            if (nxt, now) == banned or (now, nxt) == banned:
                continue
            if not visited[nxt]:
                size += 1
                visited[nxt] = True
                q.append(nxt)
    return size
                
def solution(n, wires):
    answer = 10**9
    # 트리 만들어주기
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in wires:
        size = bfs(a, (a,b), n, graph) # a를 시작 노드로 하고 (a,b) 간선을 막는 경우
        answer = min(answer, abs(n-2*size))
    return answer