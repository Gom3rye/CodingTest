import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m = map(int, input().split()) # 연구소 크기<=50, #바이러스 <=10
    board = [list(map(int, input().split())) for _ in range(n)]
    candidates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                candidates.append((i, j))
    min_time = INF
    for comb in combinations(candidates, m):
        q = deque(comb)
        time = [[-1]*n for _ in range(n)]
        for i, j in comb:
            time[i][j] = 0 # 바이러스 놓은 곳이니까 시간 초기화
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    time[i][j] = -2 # 벽은 못 가니까 나중에 도달 가능 여부 체크할 때를 위해 임의의 값 넣어주기
        # 나중에 time.count(-1) != 0: print(-1)로 불가능한 경우 체크하면 됨
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
        if any(-1 in row for row in time):
            continue
        min_time = min(min_time, max(map(max, time)))
    print(min_time if min_time != INF else -1)
solution()