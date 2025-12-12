import sys
from collections import deque
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t): # <=100
        n = int(input()) # 팀의 수 <=500
        last_rankings = list(map(int, input().split()))
        # 순서가 있는 DAG -> 위상정렬
        # 누가 누구 앞인지 모든 순서 관계를 저장하는 graph (이를 근거로 indegree 변화시키는 것, graph[a][b] = True면 a가 b보다 놓은 등수인것)
        graph = [[False]*(n+1) for _ in range(n+1)]
        indegree = [0]*(n+1)
        for i in range(n):
            for j in range(i+1, n):
                a, b = last_rankings[i], last_rankings[j]
                graph[a][b] = True # 순서 관계 저장
                indegree[b] += 1
        
        m = int(input()) # 순위 변동한 쌍 <=25000
        if m == 0:
            print(*last_rankings)
            continue
    
        # 간선 뒤집기
        for _ in range(m):
            a, b = map(int, input().split())
            # (a, b) 사이 누가 더 높게 바뀌었다가 아니라 그냥 둘의 간선이 바뀌었다의 정보만 주는 거 주의!!!
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indegree[a] += 1
                indegree[b] -= 1
            else: # graph[b][a]:
                graph[a][b] = True
                graph[b][a] = False
                indegree[a] -= 1
                indegree[b] += 1

        # print(graph)
        # print(indegree)
        q = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        answer = []
        uncertain = False # ? 판단
        count = 0
        while q:
            now = q.popleft()
            count += 1
            answer.append(now)
            # indegree 0인건 1개여야 하고 1개를 꺼냈으니까 0이어야 한다.
            if len(q) > 0:
                uncertain = True
                break
            # 다음 노드 찾기
            for nxt in range(1, n+1):
                if graph[now][nxt]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)

        if count < n: # 차례대로 indegree가 0인거 n개만큼 돌아야 하는데 중간에 큐가 비어 버렸다는 소리니까 사이클 확정(impossible)
            print("IMPOSSIBLE")
        elif uncertain:
            print("?")
        else:
            print(*answer)

solution()