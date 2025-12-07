import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline
def solution():
    while True:
        w, h = map(int, input().split()) # 가로, 세로 <=20
        if w == h == 0:
            break
        board = [list(input().strip()) for _ in range(h)]
        dirty = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'o':
                    sx, sy = i, j
                elif board[i][j] == '*':
                    dirty.append((i, j))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        INF = float('inf')
        def bfs(sx, sy):
            q = deque([(sx, sy)])
            distance = [[-1]*w for _ in range(h)]
            distance[sx][sy] = 0
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<h and 0<=ny<w and board[nx][ny] != 'x' and distance[nx][ny] == -1:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx, ny))
            return distance
        
        # bfs를 출발할 각 포인트들
        points = [(sx, sy)]+dirty
        n = len(points)
        dist = [[0]*n for _ in range(n)] # bfs 거리 전처리 (모든 지점 서로 간 거리)
        reachable = True
        for i in range(n):
            p1x, p1y = points[i]
            # 포인트마다 bfs를 돌리고
            d = bfs(p1x, p1y)
            # 다른 포인트와 거리가 -1인 경우에 unreachable, print(-1)
            for j in range(n):
                p2x, p2y = points[j]
                dist[i][j] = d[p2x][p2y]
                if dist[i][j] == -1:
                    reachable = False
                    break
            if not reachable:
                break

        if not reachable:
            print(-1)
            continue # while문 위로 올라가기

        min_dist = INF
        dirty_idx = list(range(1, n))
        for perm in permutations(dirty_idx): # dirty개수만큼 팩토리얼(!)
            d = 0
            start_idx = 0
            for nxt in perm:
                d += dist[start_idx][nxt]
                if d >= min_dist: # 가지치기
                    break
                start_idx = nxt
            else:
                min_dist = min(min_dist, d)
        print(min_dist if min_dist < INF else -1)
solution()