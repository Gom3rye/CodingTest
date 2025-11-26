import sys
input = sys.stdin.readline
def solution():
    r, c, t = map(int, input().split()) # x, y, 몇 초 후
    board, cleaner = [], []
    for i in range(r):
        row = list(map(int, input().split()))
        board.append(row)
        if row[0] == -1:
            cleaner.append(i)
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def spread(): # 동시에 확산해야 하므로 temp 만들기
        temp = [[0]*c for _ in range(r)]
        for x in range(r):
            for y in range(c):
                # 미세먼지일 때
                if board[x][y] > 0:
                    cnt = 0
                    for dx, dy in directions:
                        nx, ny = dx+x, dy+y
                        if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
                            cnt += 1
                            temp[nx][ny] += board[x][y]//5
                    temp[x][y] += board[x][y]-board[x][y]//5*cnt
        # temp를 이용해 board 업데이트 시키기
        for x in range(r):
            for y in range(c):
                if board[x][y] != -1:
                    board[x][y] = temp[x][y]
    def purify():
        up, down = cleaner
        # 위쪽 반시계 방향부터 반대로 shifting 해주기
        # 1. 아래 -> 위
        for row in range(up-2, -1, -1):
            board[row+1][0] = board[row][0]
        # 2. 왼 -> 오
        for col in range(1, c):
            board[0][col-1] = board[0][col]
        # 3. 위 -> 아래
        for row in range(1, up+1):
            board[row-1][c-1] = board[row][c-1]
        # 4. 오 -> 왼
        for col in range(c-2, 0, -1):
            board[up][col+1] = board[up][col]
        # 새로운 공기 생성
        board[up][1] = 0

        # 아래쪽 시계 방향 반대로 shifting
        # 1. 위 -> 아래
        for row in range(down+2, r):
            board[row-1][0] = board[row][0]
        # 2. 왼 -> 오
        for col in range(1, c):
            board[r-1][col-1] = board[r-1][col]
        # 3. 아래 -> 위
        for row in range(r-2, down-1, -1):
            board[row+1][c-1] = board[row][c-1] # c-1: 0based index
        # 4. 오 -> 왼
        for col in range(c-2, 0, -1):
            board[down][col+1] = board[down][col]
        # 새로운 깨끗한 공기 생성
        board[down][1] = 0

    for times in range(t):
        spread()
        purify()

    answer = sum(sum(row) for row in board)+2 # 공기청정기 -2 해준거 상쇄
    print(answer)
solution()