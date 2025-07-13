import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution():
    N, M, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]

    # 음식물 위치 기록
    for _ in range(K):
        r, c = map(int, input().split())
        graph[r-1][c-1] = 1  # 0-based 인덱스로 저장

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0  # 방문 처리
        size = 1

        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    size += 1
        return size

    max_size = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                max_size = max(max_size, bfs(i, j))

    print(max_size)

solution()