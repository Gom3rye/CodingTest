import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
def solution():
    t = int(input()) # <=1000
    for testcase in range(1, t+1):
        k, m, p = map(int, input().split()) # 테스트 케이스 번호, #노드 <=1000, #간선
        graph = [[] for _ in range(m+1)]
        indegree = [0]*(m+1)
        for _ in range(p):
            a, b = map(int, input().split())
            graph[a].append(b) # a->b로 물 흐름
            indegree[b] += 1

        # Strahler 계산을 위해 필요한 상태 정의
        strahler = [0]*(m+1) # 각 노드의 strahler 값 저장
        max_order = [0]*(m+1) # 들어오는 간선 중 최대 Strahler 값 저장해야 하니까
        count = [0]*(m+1) # 그 최대 Strahler가 몇 개 들어왔는지 체크해야 하니까
        q = deque()
        for i in range(1, m+1):
            if indegree[i] == 0:
                q.append(i)
                strahler[i] = 1 # 근원 노드들은 Strahler 값 1

        while q:
            now = q.popleft()
            # now: strahler값 확정된 노드, nxt: strahler값을 구해야 하는 노드
            # 주의!!) 모든 dp배열은 nxt 기준으로 갱신, 부모(now)의 값으로 자식(nxt)의 정보를 누적해서 indegree 0이 되면 확정한다.
            for nxt in graph[now]:
                # max_order, count 값 계산
                if strahler[now] > max_order[nxt]: # 지금 nxt의 최대 strahler값 보다 now의 strahler값이 크다면
                    max_order[nxt] = strahler[now] # 갱신
                    count[nxt] = 1
                elif strahler[now] == max_order[nxt]:
                    count[nxt] += 1
                # 진입 차수 제거
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    if count[nxt] >= 2:
                        strahler[nxt] = max_order[nxt]+1
                    else: # count값 1개인 경우
                        strahler[nxt] = max_order[nxt]
                    q.append(nxt)
        
        print(f"{k} {strahler[-1]}")
solution()