import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    # 그래프 생성 및 진입 차수 배열 초기화
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(m):
        pre, next = map(int, input().split())
        graph[pre].append(next)
        indegree[next] += 1
    
    # 초기 힙 설정
    # 집입 차수가 0인 문제들(선수 문제 없는)을 최소 힙에 넣음
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    
    result = []
    # 위상 정렬 실행
    while q:
        # 현재 풀 수 있는 문제들 중 가장 번호가 작은 문제가 pop됨
        current = heapq.heappop(q)
        result.append(current)

        # 현재 문제를 풀었으므로 이 문제와 연관된 다음 문제들의 진입 차수 감소
        for next in graph[current]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(q, next)
                
    print(*result)
solution()