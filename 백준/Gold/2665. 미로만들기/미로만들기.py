import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    # 흰 방(1) 은 가중치 0, 검은 방(0) 은 가중치 1 => 0-1 BFS
    distance = [[-1]*n for _ in range(n)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(x,y):
        q = deque([(x,y)])
        distance[x][y] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<n and maze[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y]
                    q.appendleft((nx, ny))
                elif 0<=nx<n and 0<=ny<n and maze[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    bfs(0,0)
    print(distance[n-1][n-1])
solution()