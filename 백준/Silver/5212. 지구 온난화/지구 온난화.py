import sys
input = sys.stdin.readline
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    can_save = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'X':
                danger = 0
                for dx, dy in directions:
                    nx, ny = dx+i, dy+j
                    if not (0<=nx<n and 0<=ny<m):
                        danger += 1
                    elif board[nx][ny] == '.':
                        danger += 1
                if danger <= 2:
                    can_save.append((i, j))

    max_x = max(x for x, _ in can_save)
    min_x = min(x for x, _ in can_save)
    max_y = max(y for _, y in can_save)
    min_y = min(y for _, y in can_save)
        
    new_board = [['.']*(max_y-min_y+1) for _ in range(max_x-min_x+1)]
    # 살아남을 땅만 X 표시 (줄어든 범위만큼 위로 올라가야 하니까 -min_x, -min_y 해주기)
    for x, y in can_save:
        new_board[x-min_x][y-min_y] = 'X'

    for row in new_board:
        print("".join(row))

solution()