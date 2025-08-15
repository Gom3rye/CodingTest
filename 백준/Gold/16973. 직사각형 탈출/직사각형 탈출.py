from collections import deque

def solution():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    H, W, Sr, Sc, Fr, Fc = map(int, input().split())

    # 0-based indexing
    Sr -= 1
    Sc -= 1
    Fr -= 1
    Fc -= 1

    # 누적합 배열 생성
    acc = [[0] * (M + 1) for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            acc[r][c] = grid[r - 1][c - 1] + acc[r - 1][c] + acc[r][c - 1] - acc[r - 1][c - 1]

    def is_valid(r, c):
        r2, c2 = r + H, c + W
        if r2 > N or c2 > M:
            return False
        total = acc[r2][c2] - acc[r2][c] - acc[r][c2] + acc[r][c]
        return total == 0

    visited = [[-1] * M for _ in range(N)]
    q = deque()
    q.append((Sr, Sc))
    visited[Sr][Sc] = 0

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        r, c = q.popleft()
        if (r, c) == (Fr, Fc):
            print(visited[r][c])
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                if is_valid(nr, nc):
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    print(-1)
solution()