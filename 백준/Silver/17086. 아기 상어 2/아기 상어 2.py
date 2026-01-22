import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # <=50
    board = [list(map(int, input().split())) for _ in range(n)]
    # 안전 거리의 최댓값 출력 -> 모든 상어와의 거리를 고려해야 하므로 multi-source bfs
    sharks = []
    distance = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                sharks.append((i, j))
                distance[i][j] = 0
    q = deque(sharks)
    while q:
        x, y = q.popleft()
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1)]:
            if not (0<=nx<n and 0<=ny<m):
                continue
            if distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y]+1
                q.append((nx, ny))
    print(max(map(max, distance)))
solution()