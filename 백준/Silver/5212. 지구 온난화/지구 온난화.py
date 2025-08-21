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

    # 50년 후에도 살아 있을 땅 사이즈대로 새롭게 지도 출력                
    max_x, max_y, min_x, min_y = 0, 0, float('inf'), float('inf')
    for x, y in can_save:
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
        
    new_board = [['.']*(max_y-min_y+1) for _ in range(max_x-min_x+1)]
    # 살아남을 땅만 X 표시 해주고
    for x, y in can_save:
        new_board[x-min_x][y-min_y] = 'X'

    for row in new_board:
        print("".join(row))

solution()