import sys
from collections import deque
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        last_rank = list(map(int, input().split()))
        
        # 그래프 초기화
        graph = [[False]*(n+1) for _ in range(n+1)]
        indegree = [0]*(n+1)
        
        # 작년 순위 기준으로 DAG 구성
        for i in range(n):
            for j in range(i+1, n):
                a = last_rank[i]
                b = last_rank[j]
                graph[a][b] = True
                indegree[b] += 1
        
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            # 기존 방향이 a->b였다면 → 뒤집기
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indegree[b] -= 1
                indegree[a] += 1
            else:
                graph[b][a] = False
                graph[a][b] = True
                indegree[a] -= 1
                indegree[b] += 1
        
        # 위상정렬
        q = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
        
        result = []
        certain = True
        impossible = False
        
        for _ in range(n):
            if not q:  # 사이클 존재
                impossible = True
                break
            
            if len(q) > 1:  # 순위 여러 개 가능 → 확정 불가
                certain = False
            
            now = q.popleft()
            result.append(now)
            for nxt in range(1, n+1):
                if graph[now][nxt]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)
        
        if impossible:
            print("IMPOSSIBLE")
        elif not certain:
            print("?")
        else:
            print(*result)

solution()