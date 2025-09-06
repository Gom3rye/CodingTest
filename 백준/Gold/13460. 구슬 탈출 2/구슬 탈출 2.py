import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                rx, ry = x, y
            elif board[x][y] == 'B':
                bx, by = x, y
    visited = {(rx, ry, bx, by)}
    q = deque([(rx, ry, bx, by, 0)]) # 빨간 구슬, 파란 구슬 위치, 이동 횟수
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    # 구슬을 굴리는 함수
    def move(x, y, dx, dy):
        move_dist = 0
        # 다음 칸이 벽이 아니고, 현재 칸이 구멍이 아닐 동안 계속 이동
        while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
            x += dx
            y += dy
            move_dist += 1
        return x, y, move_dist
    
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count >= 10:
            continue # 해당 상태는 실패이므로 pass
        
        # 네 방향으로 기울이기
        for dx, dy in directions:
            nrx, nry, r_dist = move(rx, ry, dx, dy) # r_dist 필요한 이유: 충돌 때 뒤로 보낼 구슬 판단하기 위해서
            nbx, nby, b_dist = move(bx, by, dx, dy)

            # 파란 구슬이 구멍에 빠지면 실패 (빨간 구슬과 함께 빠져도 실패)
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                print(count+1)
                return
            
            # 두 구슬이 같은 위치에 멈춘 경우, 더 많이 움직인 구슬을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if r_dist > b_dist:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            
            # 새로 만들어진 상태가 아직 방문 전이라면 큐에 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, count+1))
    # 10번 안에 성공하지 못했다면
    print(-1)
solution() 