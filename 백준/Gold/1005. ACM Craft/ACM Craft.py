import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def solution():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        build = [0]+list(map(int, input().split()))
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            pre, next = map(int, input().split())
            graph[next].append(pre) # pre를 다 끝내야먄 next 할 수 있다.
        w = int(input()) # 세워야 하는 건물
        dp = [-1] *(n+1) # dp[i]: i번 건물을 세우는데 드는 최소 시간 (0도 될 수 있으니까 -1로 초기화 하자)
        def dfs(next):

            if dp[next] != -1: # 이미 구한 것은 또 구하지 않기 위해
                return dp[next]
            
            dp[next] = build[next]
            
            for pre in graph[next]:
                if dp[pre] == -1:
                    dfs(pre)
                # print(f"next: {next}, pre: {pre}") 
                dp[next] = max(dp[next], dp[pre]+build[next])
                    
                # print(f"dp[{next}]:{dp[next]}, dp[{pre}]: {dp[pre]}")                   

        dfs(w)
        print(dp[w])
solution()