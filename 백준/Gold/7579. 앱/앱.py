import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    dp = {0:0} # dp[cost] = cost에 확보할 수 있는 최대 memory
    # 최소 비용에 최대 메모리를 갖도록 해야 한다.
    for mem, c in zip(memory, cost):
        temp = {}
        for dp_c, dp_mem in dp.items(): # key, value
            nm, nc = dp_mem+mem, dp_c+c
            if dp.get(nc, -1) < nm:
                temp[nc] = nm
        dp.update(temp)
    min_cost = float('inf')
    for c, mem in dp.items():
        if mem >= m:
            min_cost = min(min_cost, c)
    print(min_cost)
solution()