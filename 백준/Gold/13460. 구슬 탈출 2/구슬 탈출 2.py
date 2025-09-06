import sys
from collections import deque # 최소 횟수 구해야 하니까 bfs
input = sys.stdin.readline
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    # 파란 구슬이 빠지거나 빨간 구슬과 파란 구슬 동시에 빠지면 실패
    # 10번 초과로 움직여야 하면 -1 출력
    visited = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                srx, sry = i, j
            elif board[i][j] == 'B':
                sbx, sby = i, j

    # 벽이나 구슬을 만날 때까지 계속 기울이기
    def move(x, y, dx, dy):
        nx, ny = dx+x, dy+y
        dist = 1
        while board[nx][ny] != '#':
            if board[nx][ny] == 'O':
                return (nx, ny, dist)
            nx += dx
            ny += dy
            dist += 1
        # board[nx][ny] == '#' 이니까 그 전 좌표와 거리 주기
        nx -= dx
        ny -= dy
        dist -= 1
        return (nx, ny, dist)

    q = deque([(srx, sry, sbx, sby, 0)])
    visited.add((srx, sry, sbx, sby))
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        # print(rx, ry, bx, by, cnt)
        if cnt == 10:
            print(-1)
            return
        
        for dx, dy in directions:
            nrx, nry, rdist = move(rx, ry, dx, dy)
            nbx, nby, bdist = move(bx, by, dx, dy)

            if (nrx, nry, nbx, nby) in visited:
                continue

            if board[nbx][nby] == 'O':
                continue # 바로 print(-1) 해버리면 R가 구멍에 들어가는 시간이 좀 더 걸릴 경우를 고려 안하니까 안됨

            if board[nrx][nry] == 'O':
                print(cnt+1)
                return
            
            if (nrx, nry) == (nbx, nby): # 위치가 곂칠 때
                if rdist < bdist:
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy
            
            q.append((nrx, nry, nbx, nby, cnt+1))
            visited.add((nrx, nry, nbx, nby))
    print(-1) # R 사방이 #으로 막혀서 못 갈 때
solution()