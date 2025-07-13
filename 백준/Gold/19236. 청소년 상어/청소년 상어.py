import sys
input = sys.stdin.readline
from copy import deepcopy
def solution():
    directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] # 0~7번 방향
    initial_sea = [[None]*4 for _ in range(4)]
    fish_locations = [None]*17 # n번 fish의 좌표를 미리 저장해놓기

    for i in range(4):
        data = list(map(int, input().split()))
        for j in range(4):
            fish_num, dir = data[2*j], data[2*j+1]-1 # direction은 0~7까지니까
            initial_sea[i][j] = [fish_num, dir]
            fish_locations[fish_num] = (i,j)

    def move_fish(sea, fish_loc, sx, sy): # 계속 바뀌는 sea, fish_loc의 정보를 받아와야 하고 상어의 위치로는 fish를 옮기면 안되니까 상어 위치도 받아오기
        for i in range(1, 17): # 1~16까지의 fish 다 이동시키기
            # 이미 잡아먹힌 물고기는 pass
            if fish_loc[i] is None:
                continue
            # i번 물고기 위치 이동하기 위해 정보 저장해놓기
            x, y = fish_loc[i] # 위치 저장
            dir = sea[x][y][1] # 방향 번호로 저장
            # 이동 가능한 방향 8개 중에 가능한 방향으로 이동
            for _ in range(8): 
                dx, dy = directions[dir]
                nx, ny = x+dx, y+dy
                # 바다 안에 있고 상어 위치가 아니라면
                if 0<=nx<4 and 0<=ny<4 and not (sx == nx and sy == ny):
                    # 새로 바꾸려는 곳에 물고기가 있다면
                    if sea[nx][ny] is not None:
                        # 해당 물고기 번호 저장하고 위치 바꿈
                        other_fish = sea[nx][ny][0]
                        fish_loc[other_fish] = (x,y)
                    # swap 하고 위치 바꾸고 방향 저장
                    sea[nx][ny], sea[x][y] = sea[x][y], sea[nx][ny]
                    fish_loc[i] = (nx, ny)
                    sea[nx][ny][1] = dir
                    # 위치 정보와 방향 정보 다 바꿨으니 반복문 나오기
                    break
                # dir가 이동 가능한 방향이 아니었다면 45도 회전 (1~8까지의 d)
                dir = (dir+1)%8
    
    max_score = 0
    def backtracking(sea, fish_loc, sx, sy, score):
        nonlocal max_score
        # 현재 상태를 깊은 복사해서 이후의 재귀 분기에서 원본 데이터를 훼손하지 않도록 하기 위해서
        # 이전 상태를 그대로 유지한 채로 새로운 분기를 시도해야 하므로 깊은 복사로 원본과 분리된 복사본을 만들어야 한다.
        sea, fish_loc = deepcopy(sea), deepcopy(fish_loc)
        # 상어가 먹은 물고기의 숫자와 방향을 저장
        eaten_fish, shark_dir = sea[sx][sy]
        score += eaten_fish
        max_score = max(max_score, score)
        # 상어가 먹은 물고기를 None으로 저장
        sea[sx][sy] = None
        fish_loc[eaten_fish] = None
        # 상어가 물고기 한 마리를 먹었으니 물고기 전체 이동
        move_fish(sea, fish_loc, sx, sy)
        # 또 다시 먹을 물고기 탐색
        for i in range(1, 4):
            dx, dy = directions[shark_dir]
            nx, ny = sx+dx*i, sy+dy*i
            # 범위 안에 있고 먹을 수 있는 물고기를 먹기
            if 0<=nx<4 and 0<=ny<4 and sea[nx][ny] is not None:
                backtracking(sea, fish_loc, nx, ny, score)

    backtracking(initial_sea, fish_locations, 0, 0, 0) # sx, sy, score
    print(max_score)
solution()