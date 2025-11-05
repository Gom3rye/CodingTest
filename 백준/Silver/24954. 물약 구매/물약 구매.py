import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input()) # 물약 <=10
    costs = list(map(int, input().split())) # 가격 <=1000
    discount = [[] for _ in range(n)] # discount[i] = (a, d) 포션i를 사면 포션a를 d만큼 할인해준다.
    for i in range(n):
        m = int(input()) # 할인 정보 <=n-1
        for _ in range(m):
            a, d = map(int, input().split()) # 물약번호, 할인되는 가격
            discount[i].append((a-1, d)) # (potion index, discount)

    min_cost = float('inf')
    for perm in permutations(range(n), n):
        cost = 0
        new_costs = costs[:]
        for p in perm:
            cost += new_costs[p]
            if cost > min_cost:
                break
            for idx, discnt in discount[p]:
                new_costs[idx] = max(1, new_costs[idx]-discnt)
        min_cost = min(min_cost, cost)
    print(min_cost)
solution()