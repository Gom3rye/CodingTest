import sys
sys.setrecursionlimit(10**6)
from itertools import combinations
input = sys.stdin.readline
def solution():
    n = int(input())
    ppl = [0]+list(map(int, input().split())) # 1based index
    graph = [[] for _ in range(n+1)] # 1based index
    for i in range(1, n+1):
        nodes = list(map(int, input().split()))
        graph[i] = nodes[1:]

    def dfs(now, region, visited):
        for nxt in graph[now]:
            if nxt in region and nxt not in visited:
                visited.add(nxt)
                dfs(nxt, region, visited)
        return visited

    def is_connected(region):
        # 노드들 연결 여부 파악하는 거니까 bfs/dfs
        now = next(iter(region)) # 무작위 하나 고르기
        return dfs(now, region, {now}) == region

    min_diff = float('inf')
    all_regions = set(range(1, n+1))
    for i in range(1, n//2+1): # 선거구1의 구역 수
        for c in combinations(range(1, n+1), i):
            az1 = set(c)
            az2 = all_regions-az1
            if is_connected(az1) and is_connected(az2):
                diff = abs(sum(ppl[i] for i in az1)-sum(ppl[j] for j in az2))
                min_diff = min(min_diff, diff)
    print(min_diff if min_diff != float('inf') else -1)
solution()