import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 쉼터 수, 연결하는 길의 수
    heights = [0]+list(map(int, input().split())) # 각 쉼터의 높이
    # DAG 문제 -> 높이가 낮은 곳에서 높은 곳으로만 가는 단방향 그래프 생성
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if heights[a] > heights[b]:
            graph[b].append(a)
        else: # heights[a] < heights[b]:
            graph[a].append(b)
    # memoization 가능
    dp = [-1]*(n+1) # dp[i]: i쉼터에서 출발해서 산을 오를 때 최대로 방문할 수 있는 쉼터의 개수
    
    def dfs(now):
        # memoization
        if dp[now] != -1:
            return dp[now]
        
        cnt = 1
        for nxt in graph[now]:
            cnt = max(cnt, dfs(nxt)+1)
        dp[now] = cnt
        return dp[now]
    
    for i in range(1, n+1):
        if dp[i] == -1:
            dfs(i)
        print(dp[i]) 
solution()