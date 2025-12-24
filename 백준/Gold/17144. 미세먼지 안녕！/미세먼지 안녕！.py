import sys
input = sys.stdin.readline
def solution():
    r, c, t = map(int, input().split()) # x <=50, y <=50, 몇 초 후 <=1000
    board = [list(map(int, input().split())) for _ in range(r)]
    for i in range(r):
        if board[i][0] == -1:
            upper = i
            lower = i+1
            break
    def spread():
        # 모든 칸에서 동시에 일어남 -> temp 만들어서 나중에 한꺼번에 갱신
        temp = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] > 0: # 미세먼지가 있다면
                    cnt = 0
                    amount = board[i][j]//5
                    for nx, ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
                            cnt += 1
                            temp[nx][ny] += amount
                    temp[i][j] += board[i][j]-amount*cnt
        # 동시에 update
        for i in range(r):
            for j in range(c):
                if board[i][j] != -1:
                    board[i][j] = temp[i][j]

    def purify():
        # 윗부분 row: 0 ~ upper
        # 위->아래
        for row in range(upper-2, -1, -1):
            board[row+1][0] = board[row][0]
        # 오른->왼
        for col in range(1, c):
            board[0][col-1] = board[0][col]
        # 아래->위
        for row in range(1, upper+1):
            board[row-1][c-1] = board[row][c-1]
        # 왼->오른
        for col in range(c-2, 0, -1):
            board[upper][col+1] = board[upper][col]
        board[upper][1] = 0 # 새로운 공기 생성
        # 아랫부분 row: lower ~ r-1
        # 아래->위
        for row in range(lower+2, r):
            board[row-1][0] = board[row][0]
        # 오른->왼
        for col in range(1, c):
            board[r-1][col-1] = board[r-1][col]
        # 위->아래
        for row in range(r-2, lower-1, -1):
            board[row+1][c-1] = board[row][c-1]
        # 왼->오른
        for col in range(c-2, 0, -1):
            board[lower][col+1] = board[lower][col]
        board[lower][1] = 0
    for _ in range(t):
        spread()
        purify()

    print(sum(map(sum, board))+2) # 공기청정기 -2 고려
solution()