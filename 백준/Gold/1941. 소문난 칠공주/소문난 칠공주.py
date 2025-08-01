import sys
from collections import deque
from itertools import combinations

# 5x5 학생들의 자리
board = [list(sys.stdin.readline().strip()) for _ in range(5)]
# 25개의 모든 좌표 (0,0) ~ (4,4)
coords = [(r, c) for r in range(5) for c in range(5)]
# 25개의 좌표 인덱스 (0~24)
indices = list(range(25))

# 1. 25명 중 7명을 뽑는 모든 조합 생성
# C(25, 7) = 480,700
possible_groups = combinations(indices, 7)

answer = 0

for group in possible_groups:
    
    som_count = 0
    # 현재 조합(group)의 실제 좌표와 이다솜파 학생 수를 구함
    # BFS 탐색의 효율을 위해 set으로 저장
    group_coords = set()
    for index in group:
        r, c = coords[index]
        group_coords.add((r, c))
        if board[r][c] == 'S':
            som_count += 1

    # 2. '이다솜파'가 4명 미만이면 해당 조합은 버림
    if som_count < 4:
        continue

    # 3. 7명이 모두 연결되었는지 BFS로 확인
    q = deque()
    # 시작점은 조합의 첫 번째 학생
    start_node = next(iter(group_coords))
    q.append(start_node)
    
    visited_bfs = {start_node}
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 다음 위치가 유효하고, 현재 조합에 포함되어 있으며, 아직 방문 안했다면
            if (nr, nc) in group_coords and (nr, nc) not in visited_bfs:
                visited_bfs.add((nr, nc))
                q.append((nr, nc))
    
    # BFS가 끝난 후, 방문한 노드 수가 7개라면 모두 연결된 것
    if len(visited_bfs) == 7:
        answer += 1

print(answer)