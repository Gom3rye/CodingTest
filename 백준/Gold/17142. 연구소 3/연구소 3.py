import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 0: 빈 칸, 1: 벽, 2: 바이러스
    viruses = []
    empty = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                viruses.append((i,j))
            elif board[i][j] == 0:
                empty += 1 # 빈 공간 개수 저장

    def bfs(active):
        visited = [[-1]*n for _ in range(n)]
        q = deque()
        for x,y in active:
            q.append((x,y))
            visited[x][y] = 0 # 활성 바이러스부터 시작이니까 방문 처리
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        filled, max_time = 0, 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if board[nx][ny] == 0: # 빈 칸일 때 최대 시간 저장해줘야 함
                        max_time = max(max_time, visited[nx][ny])
                        filled += 1 # 빈칸 하나 채웠으니
        return max_time if filled == empty else float('inf')

    min_time = float('inf')
    for vir in combinations(viruses, m):
        min_time = min(min_time, bfs(vir))

    print(min_time if min_time != float('inf') else -1)
solution()