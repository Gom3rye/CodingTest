import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    castle = [list(map(int, input().split())) for _ in range(M)]

    room = [[-1]*N for _ in range(M)]
    room_size = []

    # 방향: 서, 북, 동, 남
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    wall = [1, 2, 4, 8]

    def bfs(sx, sy, idx):
        q = deque([(sx, sy)])
        room[sx][sy] = idx
        size = 1

        while q:
            x, y = q.popleft()
            for d in range(4):
                if castle[x][y] & wall[d]:
                    continue
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < M and 0 <= ny < N:
                    if room[nx][ny] == -1:
                        room[nx][ny] = idx
                        q.append((nx, ny))
                        size += 1
        return size

    # 1️⃣ 방 나누기
    idx = 0
    for i in range(M):
        for j in range(N):
            if room[i][j] == -1:
                room_size.append(bfs(i, j, idx))
                idx += 1

    # 1번, 2번 답
    print(len(room_size))
    print(max(room_size))

    # 3️⃣ 벽 하나 제거
    ans = 0
    for i in range(M):
        for j in range(N):
            for d in range(4):
                if castle[i][j] & wall[d]:
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < M and 0 <= nj < N:
                        a = room[i][j]
                        b = room[ni][nj]
                        if a != b:
                            ans = max(ans, room_size[a] + room_size[b])

    print(ans)

solution()