import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input()) # 물약 <=10 (10! ~> 3백만, 완탐 가능)
    costs = list(map(int, input().split())) # 가격 <=1000
    potions = [[] for _ in range(n)] # potion[i] = (a, d) 포션i를 사면 포션a를 d만큼 할인해준다.
    for i in range(n):
        m = int(input()) # 할인 정보 <=n-1
        if m == 0:
            continue
        for _ in range(m):
            a, d = map(int, input().split()) # 물약번호, 할인되는 가격
            potions[i].append((a-1, d)) # potion index, discount
    
    min_cost = float('inf')
    for perm in permutations(range(n), n):
        cost = 0
        new_costs = costs[:]
        for p in perm:
            cost += new_costs[p]
            for idx, discount in potions[p]:
                new_costs[idx] = max(1, new_costs[idx]-discount)
        min_cost = min(min_cost, cost)
    print(min_cost)
solution()