import sys
from itertools import combinations
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 작업 개수, 작업 순서, 실행 시간 0초로 바꿀 수 있는 개수
    t = [0]+list(map(int, input().split())) # 1based index
    # 정확히 k개의 작업의 실행시간을 강제로 0초로 바꾸었을 때 모든 작업이 완료되는 데에 최소 시간 구하기
    graph = [[] for _ in range(n+1)]
    starts = set()
    for _ in range(1, m+1):
        s, e = map(int, input().split())
        graph[e].append(s) # graph[nxt] = pre
        starts.add(s)
    all_range = set(range(1, n+1))
    end = next(iter(all_range-starts))
    
    def dfs(nxt):
        if dp[nxt] != -1:
            return dp[nxt]
        max_pre = 0
        for pre in graph[nxt]:
            max_pre = max(max_pre, dfs(pre))
        dp[nxt] = max_pre+tmp[nxt]
        return dp[nxt]
    
    min_time = float('inf')
    comb_range = set(range(2, n+1))-{end}
    for c in combinations(comb_range, k):
        dp = [-1]*(n+1)
        tmp = t[:] # deepcopy
        for zero in c:
            tmp[zero] = 0
        for i in range(1, n+1):
            dfs(i)
        min_time = min(min_time, dp[end])
    print(min_time)
solution()