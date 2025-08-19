import sys
from collections import deque
input = sys.stdin.readline
def solution():
    board = [list(input().strip()) for _ in range(8)]
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    q = deque([(7, 0)])
    time = 0
    while q:
        visited_this_turn = set()
        # 현재 시간에 탐색할 수 있는 모든 위치를 한 번에 처리 (시간의 흐름 정확히 시뮬레이션하기 위해서)
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if nx == 0 and ny == 7:
                    print(1)
                    return
                # 다음 위치가 유효한지 확인
                if 0<=nx<8 and 0<=ny<8:
                    if nx-time >= 0 and board[nx-time][ny] == '#':
                        continue
                    if nx-time-1 >= 0 and board[nx-time-1][ny] == '#':
                        continue
                    if (nx, ny) not in visited_this_turn:
                        visited_this_turn.add((nx, ny))
                        q.append((nx, ny))
        time += 1
        # 8초면 모든 벽이 사라져서 무조건 도착 가능
        if time >= 8:
            print(1)
            return
    # while 루프가 끝날 때까지 못하면 실패
    print(0)
solution()