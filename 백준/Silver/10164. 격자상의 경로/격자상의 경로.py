def solution():
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())

    # 경로 수 계산 함수 (DP)
    def count_paths(r1, c1, r2, c2):
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[rows - 1][cols - 1]

    # K의 좌표를 구함
    if K == 0:
        print(count_paths(0, 0, N - 1, M - 1))
    else:
        k_row = (K - 1) // M
        k_col = (K - 1) % M
        # (0,0) ~ (k_row,k_col) 까지 경로 수 * (k_row,k_col) ~ (N-1,M-1) 까지 경로 수
        ans = count_paths(0, 0, k_row, k_col) * count_paths(k_row, k_col, N - 1, M - 1)
        print(ans)

solution()
