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
    # 사람들 거리 먼저 계산해놓기
    ppl_dist = [bfs(pplx, pply) for pplx, pply in ppl]
    # 선물의 최대 개수
    max_gift = 0
    for exx, exy in exit:
        gift = 0
        for someone_dist in ppl_dist:
            # 그 출구로 갈 수 있고 사람들의 거리가 한별의 거리보다 짧거나 같아야지 선물 줄 수 있다.
            if hanbyeol_dist[exx][exy] != -1 and someone_dist[exx][exy] != -1 and hanbyeol_dist[exx][exy] >= someone_dist[exx][exy]:
                gift += 1
        max_gift = max(max_gift, gift)
    print(max_gift)        

solution()