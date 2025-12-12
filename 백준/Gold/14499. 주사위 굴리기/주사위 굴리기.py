import sys
input = sys.stdin.readline
def solution():
    # 왼쪽 상단 (0,0)
    n, m, sx, sy, k = map(int, input().split()) # 지도의 세로, 가로, x, y, 명령 개수
    # 아래쪽, ->
    board = [list(map(int, input().split())) for _ in range(n)]
    # 1:동, 2:서, 3:북, 4:남
    moves = list(map(int, input().split()))
    dice = [0]*6 # 위,북,동,서,남,바닥
    directions = [0]+[(0,1),(0,-1),(-1,0),(1,0)] # 1based index
    
    # 주사위를 굴리는 거 구현
    def roll(dir):
        if dir == 1: # 동쪽으로 돌림 <-> 서
            # 바닥(제일 나중에 갱신되는 거 저장해놓기)
            org_bottom = dice[-1]
            dice[-1] = dice[2] # 동 -> 바닥
            dice[2] = dice[0] # 위 -> 동
            dice[0] = dice[3] # 서 -> 위
            dice[3] = org_bottom # 바닥 -> 서

        elif dir == 2: # 서쪽으로 <-> 동
            org_bottom = dice[-1]
            dice[-1] = dice[3] # 서 -> 바닥
            dice[3] = dice[0] # 위 -> 서
            dice[0] = dice[2] # 동 -> 위
            dice[2] = org_bottom # 바닥 -> 동
            
        elif dir == 3: # 북쪽으로
            org_bottom = dice[-1]
            dice[-1] = dice[1] # 북 -> 바닥
            dice[1] = dice[0] # 위 -> 북
            dice[0] = dice[4] # 남 -> 위
            dice[4] = org_bottom # 바닥 -> 남

        else: # dir == 4: 남쪽으로
            org_bottom = dice[-1]
            dice[-1] = dice[4] # 남 -> 바닥
            dice[4] = dice[0] # 위 -> 남
            dice[0] = dice[1] # 북 -> 위
            dice[1] = org_bottom # 바닥 -> 북
            
    # 상단에 쓰여 있는 값 구하기
    for move in moves:
        dx, dy = directions[move]
        nx, ny = sx+dx, sy+dy
        if not (0<=nx<n and 0<=ny<m):
            continue
        if 0<=nx<n and 0<=ny<m:
            roll(move)
            sx, sy = nx, ny # 다음 업데이트를 위해서 위치 갱신
            # 이동한 칸이 0이면 바닥 -> 칸에 복사
            if board[nx][ny] == 0:
                board[nx][ny] = dice[-1]
            # 0이 아니면 칸 -> 바닥으로 복사, 칸은 0 되기
            else:
                dice[-1] = board[nx][ny]
                board[nx][ny] = 0
            # 이동할 때마다 주사위 윗면 출력
            print(dice[0])
solution()