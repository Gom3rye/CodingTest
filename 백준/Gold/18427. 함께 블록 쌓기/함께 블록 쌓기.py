def solution():
    import sys
    input = sys.stdin.readline

    MOD = 10007

    N, M, H = map(int, input().split())
    blocks = []
    for _ in range(N):
        blocks.append(list(map(int, input().split())))

    # dp[i][h]: i번째 학생까지 고려했을 때 높이 h를 만들 수 있는 경우의 수
    dp = [[0] * (H + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # 아무 학생도 선택하지 않고 높이 0 만드는 방법 1가지

    for i in range(1, N + 1):
        for h in range(H + 1):
            # 1. i번째 학생의 블록을 사용하지 않는 경우
            dp[i][h] = dp[i - 1][h]
            # 2. i번째 학생의 블록 중 하나를 사용하는 경우
            for b in blocks[i - 1]:
                if h - b >= 0:
                    dp[i][h] = (dp[i][h] + dp[i - 1][h - b]) % MOD

    print(dp[N][H])
solution()