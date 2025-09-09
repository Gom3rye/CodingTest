import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # n*n격자, 파이어볼 개수, 이동 명령한 횟수
    board = [[None]*n for _ in range(n)] # 행과 열이 연결되어 있음 -> % 사용
    directions = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}
    for _ in range(m):
        r, c, m, s, d = map(int, input().split())
        board[r-1][c-1] = [[m, d, s]] # 질량, 방향, 속력

    def move(board):
        new_board = [[None]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != None:
                    # board[i][j]가 한 개가 아닐 수 있음에 for문으로 돌기
                    for mv, dv, sv in board[i][j]:
                        s = sv % n # 속도 최적화
                        dx, dy = directions[dv]
                        # 주기에 따라 방향 바뀌는 거 아니니까 한 번에 좌표 계산 가능
                        nx, ny = (i+dx*s)%n, (j+dy*s)%n
                        if new_board[nx][ny] == None:
                            new_board[nx][ny] = [[mv, dv, sv]] # 파이어볼 이동시키기
                        else:
                            # 이미 거기에 파이어볼이 있다면 추가
                            new_board[nx][ny].append([mv, dv, sv])

        return new_board
    def modify(board):
        final_board = board
        for i in range(n):
            for j in range(n):
                if final_board[i][j] == None:
                    continue
                # 2개 이상 모인 경우
                cnt = len(final_board[i][j])
                if cnt >= 2:
                    # 합쳐지는 질량, 속력, 방향
                    sum_m, sum_s = 0, 0
                    odd, even = 0, 0 # 홀수 개수, 짝수 개수
                    for mv, dv, sv in final_board[i][j]:
                        sum_m += mv
                        sum_s += sv
                        if dv%2 == 1: # 홀수이면
                            odd += 1
                        else:
                            even += 1
                    # 4개로 나눠지기
                    modified_m, modified_s = sum_m//5, sum_s//cnt
                    # 질량이 0이면 소멸되기
                    if modified_m == 0:
                        final_board[i][j] = None
                        continue
        
                    if odd == 0 or even == 0:
                        dirs = [0, 2, 4, 6]
                    else:
                        dirs = [1, 3, 5, 7]
                    
                    final_board[i][j] = [[modified_m, dirs[0], modified_s]]
                    if final_board[i][j] != None:
                        final_board[i][j].append([modified_m, dirs[1], modified_s])
                        final_board[i][j].append([modified_m, dirs[2], modified_s])
                        final_board[i][j].append([modified_m, dirs[3], modified_s])
                else:
                    # cnt == 1인 경우
                    final_board[i][j] = board[i][j]
        return final_board
    # 이동을 k번
    for _ in range(k):
        new_board = move(board)
        # 이동이 끝난 뒤 2개 이상의 파이어볼이 있는 칸 조정
        board = modify(new_board)
    
    # 남아있는 파이어볼 질량의 합 구하기
    score = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == None:
                continue
            for infos in board[i][j]:
                score += infos[0]
    print(score)
solution()