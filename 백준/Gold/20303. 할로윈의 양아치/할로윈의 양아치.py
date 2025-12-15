import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 아이들 수 <=30,000, 친구관계 수 <=100,000, 넘으면 안되는 아이 수 <=3000
    candies = [0]+list(map(int, input().split())) # <=10,000, 1based index
    parents = list(range(n+1))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parents[b] = a
        
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)
    
    group_size = defaultdict(int)
    group_candies = defaultdict(int)
    for i in range(1, n+1):
        root = find(i)
        group_size[root] += 1
        group_candies[root] += candies[i]
    
    dp = [0]*k
    for root in group_size:
        size = group_size[root]
        if size >= k:
            continue
        candies = group_candies[root]
        for ppl in range(k-1, size-1, -1):
            dp[ppl] = max(dp[ppl], dp[ppl-size]+candies)
    print(dp[-1])
solution()