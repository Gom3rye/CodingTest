import sys
from collections import deque
input = sys.stdin.readline

def solution():
    board = [input().strip() for _ in range(8)]
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

    # q: (행, 열) - BFS는 레벨(시간) 단위로 탐색
    q = deque([(7, 0)]) 
    # visited[r][c] = True 이면, 해당 칸은 이미 최단 시간으로 방문했음
    
    time = 0

    while q:
        # 현재 시간에 탐색할 수 있는 모든 위치를 한 번에 처리
        # 이 level-order 방식이 시간의 흐름을 정확히 시뮬레이션함
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(q)):
            r, c = q.popleft()
            # 큐에서 꺼낸 현재 위치가, 현재 시간(time)에 벽과 충돌하는지 다시 확인
            # (제자리에 머물렀을 경우를 대비한 안전장치)
            if r - time >= 0 and board[r - time][c] == '#':
                continue
            # 9가지 이동/정지 경우를 모두 확인
            for dx, dy in directions:
                nr, nc = r + dx, c + dy

                # 목적지에 도달하면 성공
                if nr == 0 and nc == 7:
                    print(1)
                    return
                
                # 다음 위치가 유효한지 확인
                if 0 <= nr < 8 and 0 <= nc < 8 and not visited[nr][nc]:
                    # 1. 캐릭터가 이동할 위치(nr,nc)에 현재 벽이 없는지 확인
                    if nr - time >= 0 and board[nr - time][nc] == '#':
                        continue
                    
                    # 2. 캐릭터가 이동한 후, 벽이 그 위치로 내려오지 않는지 확인
                    # (현재 시간)에 (nr-1, nc)에 있던 벽이 다음 시간에 (nr, nc)로 내려옴
                    if nr - 1 - time >= 0 and board[nr - 1 - time][nc] == '#':
                        continue
                        
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        # 현재 시간대의 모든 이동이 끝나면 시간 증가
        time += 1
        
    # while 루프가 끝날 때까지 목적지에 도달 못하면 실패
    print(0)

solution()