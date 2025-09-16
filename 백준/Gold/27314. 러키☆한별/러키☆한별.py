import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    
    # --- 1. 입력 처리 및 초기 설정 ---
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]

    hanbyeol_pos = None
    people_pos = []
    exit_pos = []

    for r in range(N):
        for c in range(M):
            if board[r][c] == 'H':
                hanbyeol_pos = (r, c)
            elif board[r][c] == 'P':
                people_pos.append((r, c))
            elif board[r][c] == '#':
                exit_pos.append((r, c))

    # --- 2. BFS 헬퍼 함수 정의 ---
    # 특정 지점에서 모든 칸까지의 최단 거리를 계산하는 함수
    def bfs(start_r, start_c):
        q = deque([(start_r, start_c)])
        # -1은 방문 불가 또는 아직 방문 안 한 상태
        dist = [[-1] * M for _ in range(N)]
        dist[start_r][start_c] = 0

        while q:
            r, c = q.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # 격자 범위 안, 벽이 아니고, 아직 방문 안 한 곳
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'X' and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist

    # --- 3. 한별이의 최단 거리 계산 ---
    dist_H = bfs(hanbyeol_pos[0], hanbyeol_pos[1])
    
    # --- 4. 각 출구별로 받을 수 있는 선물 개수 계산 ---
    gifts_per_exit = [0] * len(exit_pos)

    # 각 사람에 대해 BFS를 한 번씩 실행
    for p_r, p_c in people_pos:
        dist_P = bfs(p_r, p_c)
        
        # 이 사람이 각 출구에 한별이보다 빨리 도착할 수 있는지 확인
        for i, (e_r, e_c) in enumerate(exit_pos):
            # 한별이와 사람 모두 해당 출구에 도달할 수 있어야 함
            if dist_H[e_r][e_c] != -1 and dist_P[e_r][e_c] != -1:
                # 사람이 한별이보다 빠르거나 같은 시간에 도착하면 선물 전달 가능
                if dist_P[e_r][e_c] <= dist_H[e_r][e_c]:
                    gifts_per_exit[i] += 1

    # --- 5. 최대 선물 개수 출력 ---
    if not gifts_per_exit:
        print(0)
    else:
        print(max(gifts_per_exit))

# 함수 호출
solution()