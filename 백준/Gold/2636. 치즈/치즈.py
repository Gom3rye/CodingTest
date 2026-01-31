import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # <=100
    board = [list(map(int, input().split())) for _ in range(n)]
    # 바깥 공기만 치즈를 갉아먹을 수 있도록=> (0,0)에서 bfs 돌리기!
    def bfs(x, y):
        q = deque([(x, y)])
        visited = [[False]*m for _ in range(n)]
        visited[x][y] = True
        gonna_melt = [] # 높을 치즈 좌표 모아두기
        while q:
            x, y = q.popleft()
            for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if board[nx][ny] == 0:
                        q.append((nx, ny))
                    else: # 치즈일때
                        gonna_melt.append((nx, ny))

        # 힌꺼번에 치즈 녹이기
        for cx, cy in gonna_melt:
            board[cx][cy] = 0          
    time, prev = 0, 0 # 전의 치즈값 저장하기 위해
    while True:
        cheese = sum(map(sum, board))
        if cheese == 0:
            break
        prev = cheese
        bfs(0,0)
        time += 1
    print(time)
    print(prev)
solution()