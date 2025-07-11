import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    sea = [list(map(int, input().split())) for _ in range(n)]

    # 초기 아기 상어 위치 찾기
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sx, sy = i, j
                sea[i][j] = 0

    directions = [(-1,0), (0,-1), (0,1), (1,0)]  # 위, 왼, 오, 아래 (우선순위 맞게 설정)
    size = 2
    eat = 0
    time = 0

    def bfs(sx, sy, size):
        visited = [[-1]*n for _ in range(n)]
        visited[sx][sy] = 0
        q = deque([(sx, sy)])

        min_dist = sys.maxsize
        fish_x, fish_y = -1, -1

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1 and sea[nx][ny] <= size:
                        visited[nx][ny] = visited[x][y] + 1
                        dist = visited[nx][ny]

                        # 먹을 수 있는 물고기 발견
                        if 0 < sea[nx][ny] < size:
                            if dist < min_dist:
                                min_dist = dist
                                fish_x, fish_y = nx, ny
                            elif dist == min_dist:
                                # 우선순위: 위 -> 왼
                                if nx < fish_x or (nx == fish_x and ny < fish_y):
                                    fish_x, fish_y = nx, ny
                        q.append((nx, ny))

        if fish_x == -1:
            return None
        else:
            return (fish_x, fish_y, min_dist)

    while True:
        result = bfs(sx, sy, size)
        if not result:
            break

        fx, fy, dist = result
        time += dist
        sea[fx][fy] = 0
        sx, sy = fx, fy
        eat += 1

        if eat == size:
            size += 1
            eat = 0

    print(time)

solution()
