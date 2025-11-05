import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    cost = list(map(int, input().split()))
    discount = [[] for _ in range(n)]
    for i in range(n):
        p = int(input())
        for _ in range(p):
            a, d = map(int, input().split())
            discount[i].append((a - 1, d))

    min_total = float('inf')

    def dfs(bought, cur_costs, total):
        nonlocal min_total
        
        # 모든 물약을 구매한 경우
        if len(bought) == n:
            min_total = min(min_total, total)
            return
        
        # 가지치기 (현재까지의 합이 이미 최소값보다 크면 의미 없음)
        if total >= min_total:
            return

        for i in range(n):
            if i in bought:
                continue

            # i번째 물약 구매
            new_cost = cur_costs[i]
            new_total = total + new_cost

            # 할인 적용
            next_costs = cur_costs[:]
            for (a, d) in discount[i]:
                next_costs[a] = max(1, next_costs[a] - d)

            dfs(bought + [i], next_costs, new_total)

    dfs([], cost, 0)
    print(min_total)

solution()