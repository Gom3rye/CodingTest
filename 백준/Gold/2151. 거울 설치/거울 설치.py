from collections import deque

# 방향: 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solve():
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    doors = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                doors.append((i, j))

    (sy, sx), (ey, ex) = doors

    # visited[y][x][dir]: (y,x)에 dir 방향으로 도착했을 때 필요한 최소 거울 수
    INF = 10**9
    visited = [[[INF]*4 for _ in range(N)] for _ in range(N)]
    dq = deque()

    # 시작점: 4방향 모두 넣음 (거울 없이 출발)
    for d in range(4):
        visited[sy][sx][d] = 0
        dq.append((sy, sx, d))

    while dq:
        y, x, d = dq.popleft()

        ny = y + dy[d]
        nx = x + dx[d]

        # 범위 벗어나거나 벽이면 스킵
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if board[ny][nx] == '*':
            continue

        # 직진할 때는 비용 증가 X
        if visited[ny][nx][d] > visited[y][x][d]:
            visited[ny][nx][d] = visited[y][x][d]
            dq.appendleft((ny, nx, d))  # 0-1 BFS: 비용 0 → appendleft

        # 거울 설치 가능 지점이면 회전 가능
        if board[ny][nx] == '!':
            # 거울을 설치하여 방향을 바꿔야 하는 경우
            # 상<->좌우 또는 하<->좌우
            for nd in turn_dirs(d):
                if visited[ny][nx][nd] > visited[y][x][d] + 1:
                    visited[ny][nx][nd] = visited[y][x][d] + 1
                    dq.append((ny, nx, nd))  # 비용 1 → append

    # 도착 문에서 4방향 중 최솟값
    print(min(visited[ey][ex]))

# 주어진 방향 d에서 거울을 설치하면 가능한 새로운 방향 반환
def turn_dirs(d):
    if d == 0 or d == 1:  # 상, 하 → 좌, 우
        return [2, 3]
    else:  # 좌, 우 → 상, 하
        return [0, 1]


if __name__ == "__main__":
    solve()
