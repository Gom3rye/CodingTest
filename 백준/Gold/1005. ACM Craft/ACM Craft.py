import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque
def solution():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        build = [-1]+list(map(int, input().split())) # 1based index
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            pre, nxt = map(int, input().split())
            graph[nxt].append(pre)
        w = int(input())
        result = [-1]*(n+1) # dp
        def dfs(x):
            if result[x] != -1:
                return result[x]
            max_time = 0
            for pre in graph[x]:
                max_time = max(max_time, dfs(pre))
            result[x] = max_time+build[x]
            return result[x]
        print(dfs(w))
solution()