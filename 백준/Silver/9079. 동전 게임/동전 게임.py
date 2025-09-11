from itertools import combinations
import sys
input = sys.stdin.readline

# 동전 뒤집기 함수
def flip(c):
    return 'H' if c == 'T' else 'T'

# 주어진 연산 조합을 board에 적용
def apply(board, ops):
    new_board = [row[:] for row in board]  # 깊은 복사
    for op in ops:
        if op == 0:  # 행 0
            for j in range(3):
                new_board[0][j] = flip(new_board[0][j])
        elif op == 1:  # 행 1
            for j in range(3):
                new_board[1][j] = flip(new_board[1][j])
        elif op == 2:  # 행 2
            for j in range(3):
                new_board[2][j] = flip(new_board[2][j])
        elif op == 3:  # 열 0
            for i in range(3):
                new_board[i][0] = flip(new_board[i][0])
        elif op == 4:  # 열 1
            for i in range(3):
                new_board[i][1] = flip(new_board[i][1])
        elif op == 5:  # 열 2
            for i in range(3):
                new_board[i][2] = flip(new_board[i][2])
        elif op == 6:  # 대각선 ↘
            for i in range(3):
                new_board[i][i] = flip(new_board[i][i])
        elif op == 7:  # 대각선 ↙
            for i in range(3):
                new_board[i][2 - i] = flip(new_board[i][2 - i])
    return new_board

# 모든 칸이 같은지 확인
def is_uniform(board):
    target = board[0][0]
    for i in range(3):
        for j in range(3):
            if board[i][j] != target:
                return False
    return True

def solution():
    T = int(input())
    for _ in range(T):
        board = [input().split() for _ in range(3)]
        min_moves = -1

        all_ops = list(range(8))  # 0~7번 연산

        # 연산 조합을 0~8개 선택해서 시도
        for r in range(0, 9):  # 연산 개수
            for ops in combinations(all_ops, r):
                temp_board = apply(board, ops)
                if is_uniform(temp_board):
                    if min_moves == -1 or r < min_moves:
                        min_moves = r

        print(min_moves)

solution()