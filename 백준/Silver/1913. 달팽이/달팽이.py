import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    num = int(input())
    board = [[0]*n for _ in range(n)]
    # (0,0), (1,1), (2,2)등 (i,i)에서 하->우->상->좌 로 도는거니까 i,i좌표 기억해놓기
    def make_board(x, y, length, val):

        i, j = x, y
        if i == j == n // 2:
            board[i][j] = val
            return
        # 하
        while i <= length-1:
            board[i][j] = val
            i += 1
            val -= 1
        i -= 1
        # 우
        j += 1
        while j <= length-1:
            board[i][j] = val
            j += 1
            val -= 1
        j -= 1
        # 상
        i -= 1
        while i >= x:
            board[i][j] = val
            i -= 1
            val -= 1
        i += 1
        # 좌
        j -= 1
        while j > y:
            board[i][j] = val
            j -= 1
            val -= 1
        
        make_board(x+1, y+1, length-1, val)

    make_board(0,0,n,n**2)
    for idx, row in enumerate(board):
        if num in row:
            nx, ny = idx+1, row.index(num)+1
        print(*row)
    print(nx, ny)
solution()