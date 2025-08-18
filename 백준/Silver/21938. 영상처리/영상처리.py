import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)  # DFS 사용할 경우 대비

def solution():
    N, M = map(int, input().split())
    image = []

    for _ in range(N):
        line = list(map(int, input().split()))
        row = []
        for i in range(0, len(line), 3):
            R, G, B = line[i], line[i+1], line[i+2]
            avg = (R + G + B) // 3
            row.append(avg)
        image.append(row)

    T = int(input())

    # 이진화
    binary = [[255 if image[i][j] >= T else 0 for j in range(M)] for i in range(N)]

    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        while q:
            cx, cy = q.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and binary[nx][ny] == 255:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(M):
            if binary[i][j] == 255 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)

solution()
