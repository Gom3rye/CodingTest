import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 도시의 수
    w = [list(map(int, input().split())) for _ in range(n)] # 비용 행렬
    visited = [False]*n
    visited[0] = True # 0번 노드부터 시작

    min_cost = int(1e9)
    def backtracking(city, visit, cost):
        nonlocal min_cost

        if cost >= min_cost:
            return # 가지치기
        
        if visit == n:
            return_cost = w[city][0]
            if return_cost > 0:
                min_cost = min(min_cost, cost+return_cost)
            return
        
        for next in range(1, n):
            if not visited[next] and w[city][next] > 0:
                visited[next] = True
                backtracking(next, visit+1, cost+w[city][next])
                visited[next] = False
    backtracking(0, 1, 0) # 0번 노드에서 시작
    print(min_cost)
solution()