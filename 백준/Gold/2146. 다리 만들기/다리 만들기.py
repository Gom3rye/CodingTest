import sys
from collections import deque
from math import comb
input = sys.stdin.readline
def solution():
    n = int(input()) # 지도의 크기 <=100
    board = [list(map(int, input().split())) for _ in range(n)]
    # 각 땅들의 좌표를 따로 저장해놓고 n개의 땅이 있다고하면 n-1개의 땅을 multi-source bfs 돌리면 된다.
    # 주위 땅들 표시
    visited = [[False]*n for _ in range(n)]
    def mark_lands(x, y, idx):
        q = deque([(x, y)])
        visited[x][y] = True
        board[x][y] = idx
        while q:
            x, y = q.popleft()
            for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    board[nx][ny] = idx
                    q.append((nx, ny))
    idx = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and not visited[i][j]:
                mark_lands(i, j, idx)
                idx += 1
    q = deque()
    dist = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                q.append((i, j))
                dist[i][j] = 0 # 땅인 곳은 다 0표시
    
    answer = float('inf')
    while q:
        x, y = q.popleft()
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if not (0<=nx<n and 0<=ny<n):
                continue
            # 한 번도 안 가본 물인 경우
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] # 섬 확장
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))
            # 서로 다른 육지를 만난 경우
            elif board[nx][ny] != board[x][y]:
                answer = min(answer, dist[nx][ny]+dist[x][y]) # (x,y)섬과 (nx,ny)섬까지의 거리 더하기
    print(answer)
solution() 