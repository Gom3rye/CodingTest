import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    build_time = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    dp = [0]*(n+1)

    for i in range(1, n+1):
        data = list(map(int, input().split()))
        build_time[i] = data[0]
        for pre in data[1:-1]: 
            graph[i].append(pre)

    def dfs(x):
        if dp[x] != 0:
            return dp[x]
        
        if not graph[x]:
            dp[x] = build_time[x]
            return dp[x]
        
        max_time = 0
        for pre in graph[x]:
            max_time = max(max_time, dfs(pre))
        
        dp[x] = max_time + build_time[x]
        return dp[x]        
    # 출력
    for i in range(1, n+1):
        print(dfs(i))
solution()