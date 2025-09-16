import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    hx, hy, ppl, exit = 0,0,[],[]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'H':
                hx, hy = i, j
            elif board[i][j] == 'P':
                ppl.append((i,j))
            elif board[i][j] == '#':
                exit.append((i,j))

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        distance = [[-1]*m for _ in range(n)]
        distance[sx][sy] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m and board[nx][ny] != 'X' and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
        return distance
    
    hanbyeol_dist = bfs(hx, hy)
    # 선물의 최대 개수
    giftperexit = [0]*len(exit)
    # 최대한 bfs를 덜 돌아야 하니까 제일 바깥 for문으로 두기
    for px, py in ppl:
        ppl_dist = bfs(px, py)
        for i, (exx, exy) in enumerate(exit):
            # 그 출구로 갈 수 있고 사람들의 거리가 한별의 거리보다 짧거나 같아야지 선물 줄 수 있다.
            if hanbyeol_dist[exx][exy] != -1 and ppl_dist[exx][exy] != -1 and hanbyeol_dist[exx][exy] >= ppl_dist[exx][exy]:
                giftperexit[i] += 1
    
    print(max(giftperexit))        

solution()