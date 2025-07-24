def solve():
    import sys
    input = sys.stdin.readline

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # dp[r][c][d]: (r,c)에 파이프의 끝이 있고 방향이 d일 때 가능한 경우의 수
    # d = 0: 가로, 1: 세로, 2: 대각선
    dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

    # 시작 위치: (0,1)에 가로 방향으로 놓여 있음
    dp[0][1][0] = 1

    for r in range(N):
        for c in range(2, N):  # 최소 (0,2)부터 시작
            if board[r][c] == 1:
                continue  # 벽이면 건너뜀

            # 가로 → 가로
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]

            # 세로 → 세로
            if r > 0:
                dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]

            # 대각선 → 대각선 (3칸 모두 비어 있어야)
            if r > 0 and board[r-1][c] == 0 and board[r][c-1] == 0:
                dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

    # 정답: (N-1,N-1)에 도달한 모든 방향의 합
    print(sum(dp[N-1][N-1]))

solve()