import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # #학생 <=10000, #친구관계 <=10000, 돈 <=10,000,000
    cost = list(map(int, input().split())) # 친구비
    parents = list(range(n))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            if cost[a] < cost[b]: # 친구비가 적은 걸 대표로 세우기(root)
                parents[b] = a
            else:
                parents[a] = b
        
    for _ in range(m):
        a, b = map(int, input().split())
        union(a-1, b-1)

    for i in range(n):
        find(i)

    parents_set = set(parents)
    total_cost = 0
    for c in parents_set:
        total_cost += cost[c]
        if total_cost > k:
            print("Oh no")
            break
    else:
        print(total_cost)

solution()