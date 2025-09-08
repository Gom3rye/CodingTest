import sys
input = sys.stdin.readline
def solution():
    r, c, m = map(int, input().split()) # m: 상어의 수
    # 상어의 이동을 구현해야 하니까 상어의 정보를 2차원 배열(board)안에서 관리하자.
    board = [[None]*c for _ in range(r)]
    for _ in range(m):
        x, y, s, d, z = map(int, input().split())
        board[x-1][y-1] = [s, d, z] # 0based index
    
    directions = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}
    # 낚시왕이 0 ~ c-1까지 이동하면서 r이 가장 작은 쪽에 있는 상어를 잡는다. -> 상어 이동
    # 낚시왕이 잡은 상어 크기의 합을 출력
    score = 0
    fisher = 0 # 낚시왕의 출발 위치
    def fishing(now):
        nonlocal score
        # row가 가장 작은 상어 잡기
        for i in range(r):
            if board[i][now] != None:
                score += board[i][now][-1]
                board[i][now] = None # 상어 잡기
                break
    # 이동 중에는 보드의 모습이 바뀌고 이를 동시에 변경하면 꼬이니까 new board를 생성해서 결과만 board에 새로 할당 (board = new_board)
    def sharks_move(board):
        new_board = [[None]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] != None:
                    speed, d, size = board[i][j]
                    # 왕복 주기로 위치 계산
                    if d in [1, 2]: # 상하 운동
                        temp_speed = speed % ((r-1)*2)
                    else: # 좌우 운동
                        temp_speed = speed % ((c-1)*2)

                    ox, oy = i, j # original_x, original_y 저장해놓기
                    for _ in range(temp_speed): # temp_speed만큼 이동
                        nx, ny = directions[d][0]+ox, directions[d][1]+oy
                        if not (0<=nx<r and 0<=ny<c): # 범위에 벗어난다면 방향 변경
                            if d == 1: d = 2
                            elif d == 2: d = 1
                            elif d == 3: d = 4
                            else: d = 3
                            nx, ny = directions[d][0]+ox, directions[d][1]+oy
                        ox, oy = nx, ny # 새로 이동한 위치 갱신
                    
                    # 새로 이동한 위치에 상어가 있다면
                    if new_board[ox][oy] != None:
                        if new_board[ox][oy][-1] > size: # 기존 상어의 상어가 현재 상어의 크기보다 크다면
                            continue
                    new_board[ox][oy] = [speed, d, size] # 상어 놓기
        return new_board
                            
    while fisher < c:
        # 낚시왕이 있는 열의 상어 잡기
        fishing(fisher)
        # 상어 이동
        new_board = sharks_move(board)
        fisher += 1
        board = new_board
    print(score)
solution()