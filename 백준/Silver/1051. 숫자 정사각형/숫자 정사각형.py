def solution():
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]

    max_side = 1  # 최소 한 칸짜리는 항상 정사각형

    for i in range(N):
        for j in range(M):
            for k in range(1, min(N - i, M - j)):
                if (board[i][j] == board[i][j + k] ==
                    board[i + k][j] == board[i + k][j + k]):
                    max_side = max(max_side, k + 1)

    print(max_side * max_side)

solution()
