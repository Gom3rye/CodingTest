import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    h, w, sr, sc, fr, fc = map(int, input().split())
    sr -= 1
    sc -= 1
    fr -= 1
    fc -= 1 # 0 based index로 바꾸기
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque([(sr, sc, 0)])
    visited = [[False]*m for _ in range(n)]
    # 벽(1)이어서 지날 수 없는 곳을 미리 visited[i][j] = True로 해놓자.
    # 벽을 덮을 수 있는 모든 블록의 좌측 상단 좌표를 visited 처리 (오른쪽 아래 기준)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                for x in range(max(0, i-h+1), i+1):
                    for y in range(max(0, j-w+1), j+1):
                        visited[x][y] = True
    while q:
        x, y, time = q.popleft()
        if x == fr and y == fc:
            print(time)
            return
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<=n-h and 0<=ny<=m-w and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, time+1))
    print(-1)
solution()