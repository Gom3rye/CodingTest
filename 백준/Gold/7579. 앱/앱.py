import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    total_cost = sum(cost)
    dp = [0] * (total_cost + 1)

    for i in range(N):
        m = memory[i]
        c = cost[i]
        # 배낭 문제: 비용을 역순으로 탐색
        for j in range(total_cost, c - 1, -1):
            dp[j] = max(dp[j], dp[j - c] + m)

    for c in range(total_cost + 1):
        if dp[c] >= M:
            print(c)
            return

    # 예외 처리 (문제 조건상 발생하지 않음)
    print(-1)
solution()