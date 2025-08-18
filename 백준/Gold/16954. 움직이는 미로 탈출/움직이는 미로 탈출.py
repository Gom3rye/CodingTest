from collections import deque
import sys
input = sys.stdin.readline

def solution():
    board = [list(input().strip()) for _ in range(8)]

    # 9방향 (8방향 + 제자리)
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

    def get_wall(t):
        temp = [['.']*8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if board[i][j] == '#':
                    if i + t < 8:
                        temp[i+t][j] = '#'
        return temp

    q = deque()
    q.append((7, 0, 0))  # x, y, time
    visited = [[[False]*9 for _ in range(8)] for _ in range(8)]

    while q:
        x, y, t = q.popleft()
        if x == 0 and y == 7:
            print(1)
            return

        wall_now = get_wall(t)
        wall_next = get_wall(t+1)

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            nt = min(t+1, 8)  # time은 8이상이면 벽이 다 사라짐
            if 0<=nx<8 and 0<=ny<8:
                if wall_now[nx][ny] == '#' or wall_next[nx][ny] == '#':
                    continue
                if not visited[nx][ny][nt]:
                    visited[nx][ny][nt] = True
                    q.append((nx, ny, nt))
    print(0)

solution()
