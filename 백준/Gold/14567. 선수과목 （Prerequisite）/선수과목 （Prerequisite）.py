import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        pre, nxt = map(int, input().split())
        graph[nxt].append(pre)
    period = [-1]*(n+1)
    def dfs(nxt):
        if period[nxt] != -1:
            return period[nxt]
        max_pre = 0
        for pre in graph[nxt]:
            max_pre = max(max_pre, dfs(pre))
        period[nxt] = max_pre + 1
        return period[nxt]
    # 모든 과목에 대해 최소 몇 학기 걸리는지 물었으니까 전체 dfs 돌리기
    for i in range(1, n+1):
        dfs(i)
    print(*period[1:])
solution()