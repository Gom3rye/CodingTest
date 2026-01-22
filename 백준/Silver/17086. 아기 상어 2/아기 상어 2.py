import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 거리 배열 (-1: 아직 방문 안 함)
    dist = [[-1]*M for _ in range(N)]
    q = deque()

    # 모든 상어 위치를 BFS 시작점으로 큐에 넣기
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))

    # 8방향
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]

    # BFS
    while q:
        r, c = q.popleft()
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    # 가장 큰 안전 거리 찾기
    ans = 0
    for i in range(N):
        for j in range(M):
            ans = max(ans, dist[i][j])

    print(ans)

solution()
