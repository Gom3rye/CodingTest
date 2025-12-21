import sys
from collections import deque
input = sys.stdin.readline
def solution():
    w, h = map(int, input().split()) #<=100
    board = [list(input().strip()) for _ in range(h)]
    # 거울의 최솟값 구하기
    lasers = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'C':
                lasers.append((i, j))
    sx, sy = lasers[0] # start point
    ex, ey = lasers[1] # end point
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0] # 왼,우,상,하
    
    INF = float('inf')
    q = deque()
    for dir in range(4):
        q.append((sx, sy, dir))
    # 상태 수: 100^2*4 = 4만 (각기 다른 좌표마다 4방향으로 들어올 수 있음)
    visited = [[[INF]*4 for _ in range(w)] for _ in range(h)]
    for dir in range(4):
        visited[sx][sy][dir] = 0
    while q:
        x, y, dir = q.popleft()
        if (x, y) == (ex, ey): # 도착지에 도착
            continue
        
        for ndir in range(4):
            nx, ny = x+dx[ndir], y+dy[ndir]
            if not (0<=nx<h and 0<=ny<w):
                continue
            if board[nx][ny] == '*':
                continue
            # 레이저로 나올 수 없는 방향 패쓰
            if (dir, ndir) in [(0,1), (1,0), (2,3), (3,2)]:
                continue
            cost = visited[x][y][dir]+(dir != ndir) # 안 같으면 +1, 같으면 +0
            if visited[nx][ny][ndir] > cost:
                visited[nx][ny][ndir] = cost
                if dir == ndir: # 직진하는 경우
                    q.appendleft((nx, ny, ndir))
                else: # 레이저 놓는 경우
                    q.append((nx, ny, ndir))
    
    answer = min(visited[ex][ey])
    print(answer)
solution()