from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, L, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    days = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(r, c, visited):
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True
        union = [(r, c)]
        total_population = A[r][c]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if L <= abs(A[x][y] - A[nx][ny]) <= R:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        union.append((nx, ny))
                        total_population += A[nx][ny]

        if len(union) > 1:
            new_pop = total_population // len(union)
            for x, y in union:
                A[x][y] = new_pop
            return True
        return False

    while True:
        visited = [[False]*N for _ in range(N)]
        moved = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    if bfs(i, j, visited):
                        moved = True
        if not moved:
            break
        days += 1

    print(days)

solution()
