import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n = int(input()) # 높이
    w = 2*n-1 # 너비
    board = [[' ']*w for _ in range(n)]
    
    def star(n, x, y): # 삼각형의 높이, 삼각형 꼭대기 좌표
        # 기본 삼각별 찍기
        if n == 3:
            board[x][y] = '*'
            board[x+1][y-1] = board[x+1][y+1] = '*'
            for col in range(y-2, y+3):
                board[x+2][col] = '*'
            return
        
        half = n//2
        star(half, x, y)
        star(half, x+half, y-half) # 23-12=11
        star(half, x+half, y+half)

    star(n, 0, n-1)
    for row in board:
        print("".join(row))
solution()