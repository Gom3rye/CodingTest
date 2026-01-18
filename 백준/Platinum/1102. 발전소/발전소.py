import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    state = input().strip()
    p = int(input())

    # 시작 mask
    start_mask = 0
    for i in range(n):
        if state[i] == 'Y':
            start_mask |= (1 << i)
 
    # 이미 조건 만족
    if bin(start_mask).count('1') >= p:
        print(0)
        return

    INF = float('inf')
    dp = [INF] * (1 << n)
    dp[start_mask] = 0

    for mask in range(1 << n):
        if dp[mask] == INF:
            continue

        for i in range(n):
            if not (mask & (1 << i)):
                continue  # i가 꺼져 있으면 사용 불가

            for j in range(n):
                if mask & (1 << j):
                    continue  # 이미 켜짐

                next_mask = mask | (1 << j) # j비트 키고
                dp[next_mask] = min(
                    dp[next_mask],
                    dp[mask] + cost[i][j]
                )

    answer = INF
    for mask in range(1 << n):
        if bin(mask).count('1') >= p:
            answer = min(answer, dp[mask])

    print(answer if answer != INF else -1)
solution()