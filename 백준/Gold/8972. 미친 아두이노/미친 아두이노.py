import sys
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')
def solution():
    r, c = map(int, input().split()) # <=100
    board = [input().strip() for _ in range(r)]
    temp = list(map(int, input().strip())) # len <=100
    operations = []
    for op in temp:
        operations.append(op-1) # 0based index로 바꾸기
    dx = [1,1,1,0,0,0,-1,-1,-1]
    dy = [-1,0,1,-1,0,1,-1,0,1] # 0~8까지의 방향 0based index
    # 빈 공간은 그냥 배경일 뿐이고, 중요한 건 'I'와 'R'의 위치뿐 -> I,R의 좌표만 관리하자!
    aduinos = set() # 중복 없을 예정이니까
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'I':
                jx, jy = i, j # jongsu
            elif board[i][j] == 'R':
                aduinos.add((i, j)) # crazy aduino

    def closer(sx,sy,ex,ey):
        shortest = INF
        ax, ay = -1, -1 # 다음 아두이노의 위치
        for x, y in [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]:
            nx, ny = x+sx, y+sy
            if not (0<=nx<r and 0<=ny<c):
                continue
            dist = abs(nx-ex)+abs(ny-ey)
            if dist < shortest:
                shortest = dist
                ax, ay = nx, ny
        return ax, ay

    # new_
    time = 1
    for op in operations:
        # 1. 종수 이동
        njx, njy = jx+dx[op], jy+dy[op]
        if (njx, njy) in aduinos: # 미친 아두이노 만나면 게임 끝
            print(f"kraj {time}")
            return
        jx, jy = njx, njy # 종수 좌표 갱신

        # 2. 미친 아두이노 이동
        new_aduinos_dict = defaultdict(int)
        for ax, ay in aduinos:
            nax, nay = closer(ax, ay, jx, jy)
            new_aduinos_dict[(nax, nay)] += 1
            if (nax, nay) == (jx, jy): # 종수가 있는 곳으로 이동했다면 게임 종료
                print(f"kraj {time}")
                return
        # 3. 아두이노가 한 곳에 2개 이상 모였을때 모인 것들 다 폭발
        new_aduinos = set()
        for nax, nay in new_aduinos_dict:
            if new_aduinos_dict[(nax, nay)] >= 2:
                continue
            new_aduinos.add((nax, nay))
            
        aduinos = new_aduinos
        time += 1

    # board 답안처럼 new_board 생성
    new_board = [['.']*c for _ in range(r)]
    new_board[jx][jy] = 'I' # 종수 갱신
    for ax, ay in aduinos:
        new_board[ax][ay] = 'R'
    for row in new_board:
        print(''.join(row))
solution()