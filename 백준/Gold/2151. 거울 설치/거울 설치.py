import sys
from collections import deque
input = sys.stdin.readline
def solution():
    # 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 하기 위해 설치해야 하는 거울의 최소 개수 구하기
    n = int(input()) # <=50
    board = [list(input().strip()) for _ in range(n)]
    # 거울 설치(1) or not(0) 최소 개수 문제니까 0-1 bfs
    # 빛은 직선으로만 갈 수 있는데 거울을 설치하면 왼쪽, 오른쪽으로 갈 수 있다(90도 회전 가능)
    dx = [-1, 1, 0, 0] # 상,하,좌,우
    dy = [0, 0, -1, 1]
    doors = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                doors.append((i, j))
    def mirror(d):
        if d in (0, 1):
            return (2, 3)
        else:
            return (0, 1)
    INF = float('inf')
    def bfs(doors):
        (sx, sy), (ex, ey) = doors
        q = deque()
        # 한 칸에 어떤 방향으로 오는지에 따라 결과 달라짐 -> distance[x][y][d]
        distance = [[[INF]*4 for _ in range(n)] for _ in range(n)]
        for d in range(4):
            q.append((sx, sy, d))
            distance[sx][sy][d] = 0
        
        while q:
            x, y, d = q.popleft()
            if (x,y) == (ex,ey): # 마지막 문에 도착
                continue
                
            nx, ny = x+dx[d], y+dy[d]
            if not (0<=nx<n and 0<=ny<n):
                continue
            if board[nx][ny] == '*':
                continue
            # 직진하는 경우
            if distance[nx][ny][d] > distance[x][y][d]:
                distance[nx][ny][d] = distance[x][y][d]
                q.appendleft((nx, ny, d))
    
            # 거울을 만나 방향 바뀌는 경우
            if board[nx][ny] == '!':
                # 거울을 /,\ 중 어느 방향으로 놓을지 모든 경우의 수 고려
                for nd in mirror(d):
                    if distance[nx][ny][nd] > distance[x][y][d]+1:
                        distance[nx][ny][nd] = distance[x][y][d]+1
                        q.append((nx, ny, nd))
        return min(distance[ex][ey])
    print(bfs(doors))
solution()