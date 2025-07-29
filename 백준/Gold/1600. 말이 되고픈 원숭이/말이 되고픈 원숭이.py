from collections import deque
import sys
input = sys.stdin.readline

def solution():
    K = int(input())  # 말처럼 이동할 수 있는 최대 횟수
    W, H = map(int, input().split())  # W: 너비, H: 높이
    board = [list(map(int, input().split())) for _ in range(H)]

    # 말이 이동할 수 있는 방향 8개
    horse_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                   (2, 1), (1, 2), (-1, 2), (-2, 1)]
    # 일반 이동 4방향
    normal_moves = [(-1,0), (1,0), (0,-1), (0,1)]

    # visited[x][y][k]: (x,y) 위치에 k번 말 점프를 사용해서 도달한 적이 있는가
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = True

    queue = deque()
    queue.append((0, 0, 0, 0))  # x, y, 말 점프 사용 수, 이동 횟수

    while queue:
        x, y, k, count = queue.popleft()

        if x == H - 1 and y == W - 1:
            print(count)
            return

        # 일반 이동
        for dx, dy in normal_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                if not visited[nx][ny][k] and board[nx][ny] == 0:
                    visited[nx][ny][k] = True
                    queue.append((nx, ny, k, count + 1))

        # 말 이동 (남은 횟수가 있는 경우만)
        if k < K:
            for dx, dy in horse_moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny][k + 1] and board[nx][ny] == 0:
                        visited[nx][ny][k + 1] = True
                        queue.append((nx, ny, k + 1, count + 1))

    # 도달할 수 없는 경우
    print(-1)

solution()