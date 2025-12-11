import sys
from collections import deque

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = None

    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input().rstrip())
            for c in range(C):
                if row[c] == 'S':
                    start = (l, r, c)
            floor.append(row)
        building.append(floor)
        input()  # 빈 줄

    # BFS 준비
    dz = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]

    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    q = deque()
    sz, sx, sy = start
    q.append((sz, sx, sy, 0))
    visited[sz][sx][sy] = True

    escaped = False

    while q:
        z, x, y, dist = q.popleft()

        if building[z][x][y] == 'E':
            print(f"Escaped in {dist} minute(s).")
            escaped = True
            break

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    q.append((nz, nx, ny, dist + 1))

    if not escaped:
        print("Trapped!")
