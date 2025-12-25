import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

black = []
white = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if (i + j) % 2 == 0:
                black.append((i, j))
            else:
                white.append((i, j))

def solve(cells):
    diag1 = [False] * (2 * N)
    diag2 = [False] * (2 * N)
    res = 0

    def dfs(idx, cnt):
        nonlocal res
        res = max(res, cnt)
        for i in range(idx, len(cells)):
            r, c = cells[i]
            d1 = r + c
            d2 = r - c + N - 1
            if not diag1[d1] and not diag2[d2]:
                diag1[d1] = diag2[d2] = True
                dfs(i + 1, cnt + 1)
                diag1[d1] = diag2[d2] = False

    dfs(0, 0)
    return res

print(solve(black) + solve(white))
