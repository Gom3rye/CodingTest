# 방향: ←, ↖, ↑, ↗, →, ↘, ↓, ↙ (1~8)
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향 (물복사 버그 전용)
diag_dx = [-1, -1, 1, 1]
diag_dy = [-1, 1, -1, 1]

def solve_magician_shark():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    moves = [tuple(map(int, input().split())) for _ in range(M)]

    # 초기 구름 위치
    clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

    for d, s in moves:
        # 1. 구름 이동
        new_clouds = []
        for x, y in clouds:
            nx = (x + dx[d-1] * s) % N
            ny = (y + dy[d-1] * s) % N
            new_clouds.append((nx, ny))

        # 2. 비 내림
        visited = [[False]*N for _ in range(N)]
        for x, y in new_clouds:
            A[x][y] += 1
            visited[x][y] = True

        # 3. 물복사 버그
        for x, y in new_clouds:
            count = 0
            for k in range(4):
                nx = x + diag_dx[k]
                ny = y + diag_dy[k]
                if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                    count += 1
            A[x][y] += count

        # 4. 새로운 구름 생성
        clouds = []
        for i in range(N):
            for j in range(N):
                if A[i][j] >= 2 and not visited[i][j]:
                    clouds.append((i, j))
                    A[i][j] -= 2

    # 결과 출력
    print(sum(map(sum, A)))

solve_magician_shark()  # 제출 시에만 호출
