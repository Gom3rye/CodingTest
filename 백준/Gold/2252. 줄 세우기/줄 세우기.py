import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 학생 수 <= 32,000, 키 비교 수 <= 100,000
    indegree = [0]*(n+1) # 진입차수
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    answer = []
    while q:
        student = q.popleft()
        answer.append(student)
        for nxt in graph[student]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    print(*answer)

solution()