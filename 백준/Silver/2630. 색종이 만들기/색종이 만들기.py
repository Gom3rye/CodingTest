import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # white: 0, blue: 1
    white_squares, blue_squares = 0, 0
    def is_valid(r, c, size):
        first_color = board[r][c]
        for i in range(r, r+size):
            for j in range(c, c+size):
                if board[i][j] != first_color:
                    return False
        return True
    def make_half(r, c, size): # 내가 맡은 구역의 시작행, 열, 한 변의 길이
        nonlocal white_squares, blue_squares
        if is_valid(r, c, size):
            if board[r][c] == 1:
                blue_squares += 1
            elif board[r][c] == 0:
                white_squares += 1
        else:
            # 4사분면으로 재귀 다시 돌리기
            size //= 2
            make_half(r, c, size) # 1사분면
            make_half(r, c+size, size) # 2사분면
            make_half(r+size, c, size) # 3사분면
            make_half(r+size, c+size, size) # 4사분면

    make_half(0,0,n) # 처음에는 (0, 0)에서 한 변의 길이가 n인 색종이 검사    
    print(white_squares)
    print(blue_squares)
solution()