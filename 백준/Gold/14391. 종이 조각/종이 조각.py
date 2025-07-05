import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, list(input().strip()))) for _ in range(n)]

    max_sum = 0

    for mask in range(1 << (n * m)):  # 2^(N*M) 가지 경우의 수
        total = 0

        # 가로 조각 계산
        for i in range(n):
            row_sum = 0
            for j in range(m):
                idx = i * m + j  # 1차원 index로 변환
                if (mask & (1 << idx)) == 0:  # 가로 조각일 때
                    row_sum = row_sum * 10 + board[i][j]
                else:
                    total += row_sum
                    row_sum = 0
            total += row_sum  # 마지막 조각 추가

        # 세로 조각 계산
        for j in range(m):
            col_sum = 0
            for i in range(n):
                idx = i * m + j
                if (mask & (1 << idx)) != 0:  # 세로 조각일 때
                    col_sum = col_sum * 10 + board[i][j]
                else:
                    total += col_sum
                    col_sum = 0
            total += col_sum  # 마지막 조각 추가

        max_sum = max(max_sum, total)
    print(max_sum)
solution()