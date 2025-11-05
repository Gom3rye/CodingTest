import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution():
    n = int(input())
    base_cost = list(map(int, input().split()))
    discount = [[] for _ in range(n)]

    for i in range(n):
        p = int(input())
        for _ in range(p):
            a, d = map(int, input().split())
            discount[i].append((a - 1, d))

    memo = {}

    def dfs(bought, cur_costs):
        # bought: frozenset(이미 산 물약 번호들)
        # cur_costs: 현재 시점의 물약 가격 리스트
        if len(bought) == n:
            return 0  # 모든 물약 구매 완료

        key = (bought, tuple(cur_costs))
        if key in memo:
            return memo[key]

        res = float('inf')

        for i in range(n):
            if i in bought:
                continue

            # i번 물약 구매
            new_cost = cur_costs[i]

            # 현재 물약 구매 후 할인 적용
            next_costs = cur_costs[:]
            for (a, d) in discount[i]:
                next_costs[a] = max(1, next_costs[a] - d)

            new_bought = bought | {i}
            res = min(res, new_cost + dfs(new_bought, next_costs))

        memo[key] = res
        return res

    print(dfs(frozenset(), base_cost))

solution()