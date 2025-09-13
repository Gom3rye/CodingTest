import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    t = int(input())
    def flip(board, operations):
        new_board = [row[:] for row in board] # 다음 연산에서 board 또 써야 하니까 깊은 복사
        for op in operations:
            # 행 연산
            if 0<=op<3:
                for j in range(3):
                    new_board[op][j] = 'T' if new_board[op][j] == 'H' else 'H'
            # 열 연산
            elif 3<=op<5:
                op -= 3
                for i in range(3):
                    new_board[i][op] = 'T' if new_board[i][op] == 'H' else 'H'
            # 대각선1
            elif op == 6:
                for i in range(3):
                    new_board[i][i] = 'T' if new_board[i][i] == 'H' else 'H'
            # 대각선2
            else:
                for i in range(3):
                    new_board[i][2-i] = 'T' if new_board[i][2-i] == 'H' else 'H'
        return new_board

    def check(board):
        # 모두 같은 면인지 확인
        if all(board[i][j]=='H' for i in range(3) for j in range(3)):
            return True
        elif all(board[i][j]=='T' for i in range(3) for j in range(3)):
            return True
        return False

    for _ in range(t):
        board = [input().split() for _ in range(3)]
        flag = False
        for cnt in range(8):
            for operations in combinations(range(8), cnt): # 연산 횟수0~2: 행 바꾸기, 3~5: 열 바꾸기, 6: 대각선1, 7: 대각선2
                new_board = flip(board, operations)
                if check(new_board):
                    print(cnt)
                    flag = True
                    break
            if flag:
                break
        # 모두 같은 면으로 만드는 것이 불가능한 경우
        if not flag:
            print(-1)
solution()