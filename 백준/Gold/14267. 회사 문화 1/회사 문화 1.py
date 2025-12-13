import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 직원수, 칭찬수 <=100,000
    boss = [0]+list(map(int, input().split())) # 1based index
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    # graph방향: 사장 -> 부장 -> 신입
    for i in range(1, n+1):
        if boss[i] == -1:
            continue
        # graph[prev].append(nxt)
        graph[boss[i]].append(i)
        indegree[i] += 1
    # 칭찬 받은 크기
    compliment = [0]*(n+1)
    # 직속 상사에게 칭찬받은 사람, 수치
    for _ in range(m):
        i, w = map(int, input().split())
        compliment[i] += w
    
    q = deque()
    # indegree 0부터(사장) 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        pre = q.popleft()
        
        for nxt in graph[pre]:
            compliment[nxt] += compliment[pre]
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append((nxt))
    print(*compliment[1:])
        
solution()