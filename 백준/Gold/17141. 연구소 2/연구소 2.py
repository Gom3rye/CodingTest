import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m = map(int, input().split()) # 연구소 크기<=50, #바이러스 <=10
    board = [list(map(int, input().split())) for _ in range(n)]
    candidates = []
    wall_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                candidates.append((i, j))
            elif board[i][j] == 1:
                wall_cnt += 1
    min_time = INF
    for comb in combinations(candidates, m):
        q = deque(comb)
        time = [[-1]*n for _ in range(n)]
        for i, j in comb:
            time[i][j] = 0 # 바이러스 놓은 곳이니까 시간 초기화
        while q:
            x, y = q.popleft()
            for nx, ny in [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]:
                if not (0<=nx<n and 0<=ny<n):
                    continue
                # 벽이 아니고 처음 방문하는 곳인 경우에만
                if board[nx][ny] != 1 and time[nx][ny] == -1:
                    time[nx][ny] = time[x][y]+1
                    q.append((nx, ny))
        # 일단 모든 바이러스를 도달 가능한지 체크
        if sum(row.count(-1) for row in time) != wall_cnt:
            continue
        min_time = min(min_time, max(map(max, time)))
    print(min_time if min_time != INF else -1)
solution()