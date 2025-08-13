import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    # 초기 구슬 구멍 위치 찾기
    rx, ry, bx, by = 0, 0, 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                rx, ry = x, y
            elif board[x][y] == 'B':
                bx, by = x, y
    visited = {(rx, ry, bx, by)}
    q = deque([(rx, ry, bx, by, 0)]) # 빨간 구슬, 파란 구슬 위치, 이동 횟수
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 벽에 닿기 전이나 구멍을 만나기 전까지 계속 직진
    def move(x, y, dx, dy):
        dist = 0
        while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
            x += dx
            y += dy
            dist += 1
        return x, y, dist

    while q:
        rx, ry, bx, by, count = q.popleft()
        # 10번 초과로 움직이면 실패
        if count >= 10:
            continue
        for dx, dy in directions:
            nrx, nry, r_dist = move(rx, ry, dx, dy)
            nbx, nby, b_dist = move(bx, by, dx, dy)
            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue
            # 빨간 구슬이 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                print(1)
                return
            # 한 곳으로 모일 때
            if (nrx, nry) == (nbx, nby):
                # 더 뒤에 있었던 구슬을 한 칸 뒤로
                if r_dist > b_dist:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            if not (nrx, nry, nbx, nby) in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, count+1))
    print(0)
solution()