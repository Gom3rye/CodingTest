from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    # 수정이 가능하도록 문자열 리스트를 2차원 리스트로 변환
    grid = [list(row) for row in storage]

    # 모든 요청을 순서대로 처리
    for req in requests:
        item_type = req[0]
        if len(req) == 2:
            # --- 크레인 작업 ---
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == item_type:
                        grid[r][c] = '.'
        else:
            # --- 지게차 작업 ---
            # 1. 외부와 연결된 빈 공간 찾기 (BFS)
            q = deque()
            visited_empty = [[False] * m for _ in range(n)]

            # 가장자리(테두리)에 있는 모든 빈 공간을 큐에 추가
            for r in range(n):
                for c in range(m):
                    if (r == 0 or r == n - 1 or c == 0 or c == m - 1) and grid[r][c] == '.':
                        if not visited_empty[r][c]:
                            q.append((r, c))
                            visited_empty[r][c] = True
            
            # BFS를 실행하여 외부와 연결된 모든 빈 공간을 visited_empty에 표시
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            while q:
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < n and 0 <= nc < m and not visited_empty[nr][nc] and grid[nr][nc] == '.':
                        visited_empty[nr][nc] = True
                        q.append((nr, nc))
            
            # 2. 접근 가능한 컨테이너를 찾아 제거
            to_remove = []
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == item_type:
                        # 인접 칸이 외부와 연결되어 있는지 확인
                        is_accessible = False
                        for i in range(4):
                            nr, nc = r + dr[i], c + dc[i]
                            # 인접 칸이 경계 밖이거나,
                            if not (0 <= nr < n and 0 <= nc < m):
                                is_accessible = True
                                break
                            # 외부와 연결된 빈 공간(visited_empty)인 경우
                            if visited_empty[nr][nc]:
                                is_accessible = True
                                break
                        if is_accessible:
                            to_remove.append((r,c))
            
            for r, c in to_remove:
                grid[r][c] = '.'

    # 남은 컨테이너 개수 세기
    count = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] != '.':
                count += 1
                
    return count
# from collections import deque
# def solution(storage, requests):
#     answer = 0
#     n, m = len(storage), len(storage[0])
#     board = [list(row) for row in storage] # 빈칸(-1)으로 바꿔야 하니까 list로(문자열은 불변)
#     for req in requests:
#         if len(req) == 2:
#             for i in range(n):
#                 for j in range(m):
#                     if board[i][j] == req[0]:
#                         board[i][j] = -1
#         else: # len() == 1
#             # 외부와 연결된 빈 공간 찾기
#             q = deque()
#             empty = [[False]*m for _ in range(n)]
#             # 테두리에 있는 모든 빈 공간을 큐에 추가
#             for i in range(n):
#                 for j in range(m):
#                     if (i==0 or i==n-1 or j==0 or j==m-1) and board[i][j] == -1:
#                         if not empty[i][j]:
#                             q.append((i, j))
#                             empty[i][j] = True
#     return answer