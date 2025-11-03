import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
def solution():
    n, m, g, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    available = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 2] # 배양 가능한 땅 좌표들
    # 0: 호수, 1: 배양액을 뿌릴 수 없는 땅, 2: 배양액을 뿌릴 수 있는 땅
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def get_flowers(green, red):
        q = deque()
        # visited로 [시간, 상태] 관리 (상태:-1(비어있음),0(g),1(r),2(꽃)) == new_board
        visited = [[[0, -1] for _ in range(m)] for _ in range(n)]
        for x, y in green:
            visited[x][y] = [0, 0]
            q.append((x, y, 0)) # 좌표, 상태
        for x, y in red:
            visited[x][y] = [0, 1]
            q.append((x, y, 1))
        flowers = 0
        while q:
            x, y, type = q.popleft()

            if visited[x][y][1] == 2: # 마지막에서 꽃이 된 경우
                continue
            time = visited[x][y][0]
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if not (0<=nx<n and 0<=ny<m):
                    continue
                if board[nx][ny] == 0: # 호수이면
                    continue
                # 아직 배양액이 안 퍼진 칸:
                if visited[nx][ny][1] == -1:
                    visited[nx][ny] = [time+1, type]
                    q.append((nx, ny, type))
                # g에 r퍼진 칸 or r에 g퍼진 칸
                elif (visited[nx][ny] == [time+1, 0] and type == 1) or (visited[nx][ny] == [time+1, 1] and type == 0):
                    visited[nx][ny] = [time+1, 2]
                    flowers += 1
        return flowers

    # 최대 꽃의 개수
    max_flowers = 0
    for green in combinations(available, g):
        left = [(i, j) for (i, j) in available if (i, j) not in green]
        for red in combinations(left, r):
            max_flowers = max(max_flowers, get_flowers(green, red))
    print(max_flowers)            
solution()