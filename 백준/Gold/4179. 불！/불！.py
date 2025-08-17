import sys
from collections import deque

input = sys.stdin.readline

def solution():
    R, C = map(int, input().split())
    maze = [list(input().strip()) for _ in range(R)]

    # --- 1. 불의 전파 시간 계산 (Fire BFS) ---
    fire_time = [[-1] * C for _ in range(R)]
    q_fire = deque()

    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'J':
                jihun_start = (r, c)
            elif maze[r][c] == 'F':
                q_fire.append((r, c))
                fire_time[r][c] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q_fire:
        r, c = q_fire.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and fire_time[nr][nc] == -1 and maze[nr][nc] != '#':
                fire_time[nr][nc] = fire_time[r][c] + 1
                q_fire.append((nr, nc))

    # --- 2. 지훈이의 탈출 경로 탐색 (Jihun BFS) ---
    q_jihun = deque([(jihun_start[0], jihun_start[1], 0)]) # (행, 열, 도착시간)
    visited_jihun = [[False] * C for _ in range(R)]
    visited_jihun[jihun_start[0]][jihun_start[1]] = True

    while q_jihun:
        r, c, time = q_jihun.popleft()

        # 네 방향으로 이동 시도
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # ✨ 수정된 부분 1: 다음 칸이 경계 밖이면 즉시 탈출 성공
            if not (0 <= nr < R and 0 <= nc < C):
                print(time + 1)
                return

            # ✨ 수정된 부분 2: 이동 조건들을 명확하게 재정리
            # 다음 칸이 (1)벽이 아니고, (2)방문한 적 없으며, (3)불보다 먼저 도착하는지 확인
            if maze[nr][nc] != '#' and not visited_jihun[nr][nc]:
                if fire_time[nr][nc] == -1 or time + 1 < fire_time[nr][nc]:
                    visited_jihun[nr][nc] = True
                    q_jihun.append((nr, nc, time + 1))
    
    # while 루프가 끝날 때까지 탈출하지 못했다면
    print("IMPOSSIBLE")

solution()