import sys
input = sys.stdin.readline
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n, m = map(int, input().split())
    # 범위를 벗어난 곳도 바다이므로 . 패딩값 주고 시작하기
    board = [['.']*(m+2)]
    for _ in range(n):
        board.append(['.']+list(input().strip())+['.'])
    board.append(['.']*(m+2))
    ready_to_disapper = []
    for i in range(n+2):
        for j in range(m+2):
            if board[i][j] == 'X':
                count = 0
                for dx, dy in directions:
                    nx, ny = dx+i, dy+j
                    if board[nx][ny] == '.':
                        count += 1
                if count >= 3:
                    ready_to_disapper.append((i, j))

    for x, y in ready_to_disapper:
        board[x][y] = '.'
    
    max_x, max_y, min_x, min_y = 0, 0, float('inf'), float('inf')
    # 패딩값 빼고 검사
    for x in range(1, n+1):
        for y in range(1, m+1):
            if board[x][y] == 'X':
                max_x = max(max_x, x)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                min_y = min(min_y, y)

    for i in range(min_x, max_x+1):
        print("".join(board[i][min_y:max_y+1]))

solution()