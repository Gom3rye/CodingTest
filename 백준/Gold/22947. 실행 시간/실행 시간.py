import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 작업 개수, 작업 순서, 실행 시간 0초로 바꿀 수 있는 개수
    t = [0]+list(map(int, input().split())) # 1based index
    # 정확히 k개의 작업의 실행시간을 강제로 0초로 바꾸었을 때 모든 작업이 완료되는 데에 최소 시간 구하기
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    starts = set()
    for _ in range(1, m+1):
        s, e = map(int, input().split())
        graph[s].append(e) # graph[pre] = nxt
        indegree[e] += 1
        starts.add(s)
    all_range = set(range(1, n+1))
    end = next(iter(all_range-starts))
    
    def topology(pre):
        tmp_indegree = indegree[:] # deepcopy
        q = deque([pre])
        while q:
            pre = q.popleft()
            for nxt in graph[pre]:
                tmp_indegree[nxt] -= 1 # pre 뺏으니까
                dp[nxt] = max(dp[nxt], dp[pre]+tmp[nxt])
                if tmp_indegree[nxt] == 0:
                    q.append(nxt)
    
    min_time = float('inf')
    comb_range = set(range(2, n+1))-{end}
    for c in combinations(comb_range, k):
        dp = [-1]*(n+1)
        dp[1] = t[1]
        tmp = t[:] # deepcopy
        for zero in c:
            tmp[zero] = 0
        topology(1)
        min_time = min(min_time, dp[end])
    print(min_time)
solution()