from collections import deque

def max_safe_areas(n, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_height = max(map(max, grid))
    result = 0

    def bfs(x, y, visited, rain_level):
        queue = deque([(x, y)])
        visited[x][y] = True
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and grid[nx][ny] > rain_level:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    for rain in range(0, max_height + 1):
        visited = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j] > rain:
                    bfs(i, j, visited, rain)
                    count += 1
        result = max(result, count)
    return result

# 입력 예제 테스트
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(max_safe_areas(n, grid))
