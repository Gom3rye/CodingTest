import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    # BFS 함수: deque를 사용하여 최적화
    def bfs(start_r, start_c):
        q = deque([(start_r, start_c)])
        dist = [[-1] * M for _ in range(N)]
        dist[start_r][start_c] = 0
        
        # H로부터의 BFS에서는 탐색 순서도 함께 반환
        bfs_order = [(start_r, start_c)] if (start_r, start_c) == hanbyeol_pos else None

        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 'X' and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    if bfs_order is not None:
                        bfs_order.append((nr, nc))
        return dist, bfs_order

    # 1. 위치 찾기
    people_pos, exit_pos = [], []
    hanbyeol_pos = None
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'H':
                hanbyeol_pos = (r, c)
            elif grid[r][c] == 'P':
                people_pos.append((r, c))
            elif grid[r][c] == '#':
                exit_pos.append((r, c))

    # 2. 거리 정보 사전 계산
    dist_H, bfs_order_H = bfs(hanbyeol_pos[0], hanbyeol_pos[1])
    dists_P = [bfs(pr, pc)[0] for pr, pc in people_pos]

    # 3. 각 칸에서 만날 수 있는 사람 집합 사전 계산
    gifts_at_cell = [[set() for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if dist_H[r][c] != -1:
                for i in range(len(people_pos)):
                    if dists_P[i][r][c] != -1 and dists_P[i][r][c] <= dist_H[r][c]:
                        gifts_at_cell[r][c].add(i)

    # 4. DP 테이블 채우기
    # dp[r][c] = (최대 선물 개수, 해당 선물 집합)
    dp = [[(0, set()) for _ in range(M)] for _ in range(N)]

    hr, hc = hanbyeol_pos
    dp[hr][hc] = (len(gifts_at_cell[hr][hc]), gifts_at_cell[hr][hc])

    # H로부터의 BFS 탐색 순서대로 DP 테이블 계산
    for r, c in bfs_order_H:
        # 현재 위치에서 얻는 선물
        current_gifts = gifts_at_cell[r][c]

        # 인접한 자식 노드들에게 현재까지의 최적해 전파
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            # 자식 노드가 최단 경로상에 있는지 확인
            if 0 <= nr < N and 0 <= nc < M and dist_H[nr][nc] == dist_H[r][c] + 1:
                
                # 부모(r,c)로부터 물려받은 선물 집합과 자식(nr,nc)에서 얻는 선물 집합을 합침
                new_gift_set = dp[r][c][1].union(gifts_at_cell[nr][nc])
                new_gift_count = len(new_gift_set)

                # 기존 자식 노드의 DP 값보다 더 많은 선물을 얻을 수 있다면 갱신
                if new_gift_count > dp[nr][nc][0]:
                    dp[nr][nc] = (new_gift_count, new_gift_set)

    # 5. 최종 답 계산
    max_gifts = 0
    for r, c in exit_pos:
        max_gifts = max(max_gifts, dp[r][c][0])

    print(max_gifts)

solution()