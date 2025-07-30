import sys
input = sys.stdin.readline
from collections import deque
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n, m = map(int, input().split())
    sea = [list(map(int, input().split())) for _ in range(n)]
    def melt():
        # 빙산을 1년간 녹이고 그 결과를 새로운 sea배열로 리턴
        new_sea = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if sea[i][j] > 0:
                    water = 0
                    for dx, dy in directions:
                        nx, ny = dx+i, dy+j
                        if 0<=nx<n and 0<=ny<m and sea[nx][ny] == 0:
                            water += 1
                    new_sea[i][j] = max(sea[i][j]-water, 0) # 뺀 결과값이 음수가 나오면 안되니까
        return new_sea

    def count_glaciers():
        # 빙산 덩어리 세기
        visited = [[False]*m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if sea[i][j] >0 and not visited[i][j]:
                    count += 1
                    # bfs 시작
                    q = deque([(i, j)])
                    visited[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = dx+x, dy+y
                            if 0<=nx<n and 0<=ny<m and sea[nx][ny] >0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
        return count
    years = 0
    while True:
        count = count_glaciers()
        if count == 0:
            print(0)
            return
        elif count >= 2:
            print(years)
            return
        sea[:] = melt()
        years += 1
solution()