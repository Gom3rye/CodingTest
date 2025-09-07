import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    build = [0]*(n+1) # build[i]:i의 작업 시간
    for i in range(1, n+1):
        data = list(map(int, input().split()))
        build[i] = data[0]
        for pre in data[2:]:
            graph[i].append(pre)
    
    dp = [-1]*(n+1) # dp[i]를 마치기 위한 최소 시간
    def dfs(nxt):
        if dp[nxt] != -1:
            return dp[nxt]
        
        max_pre = 0
        # 선행 작업이 있으면
        for pre in graph[nxt]:
            max_pre = max(max_pre, dfs(pre))
        
        dp[nxt] = max_pre + build[nxt]
        return dp[nxt]

    # 가장 오래 걸리는 시간이 모든 작업을 수행한 결과이므로
    for i in range(1, n+1):
        dfs(i)
    print(max(dp))
solution()