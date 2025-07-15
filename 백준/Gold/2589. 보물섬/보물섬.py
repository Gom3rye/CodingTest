import sys
input = sys.stdin.readline
from collections import deque
def solution():
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    n, m = map(int, input().split()) # 세로, 가로
    tm = [input().strip() for _ in range(n)]
    # 최단 거리니까 bfs를 bruteforce로 돌리기
    def bfs(x, y):
        q = deque([(x,y)])
        distance = [[-1]*m for _ in range(n)] # 중복 체크할 방문 거리 배열
        distance[x][y] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m and tm[nx][ny] == 'L' and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

        result = max(max(row) for row in distance)
        return result
    result = 0
    for i in range(n):
        for j in range(m):
            if tm[i][j] == 'L':
                result = max(result, bfs(i, j))
    print(result)
solution()