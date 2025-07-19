from collections import deque
import sys

def bfs(N, M, graph):
    # visited[x][y][0]: 벽을 부수지 않고 방문
    # visited[x][y][1]: 벽을 부수고 방문
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 0))  # x, y, 벽을 부순 여부(0 또는 1)
    visited[0][0][0] = 1  # 시작 지점은 1로 시작 (칸 수로 카운트)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, broken = queue.popleft()

        # 도착 지점에 도달했으면 종료
        if x == N - 1 and y == M - 1:
            return visited[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 있을 경우
            if 0 <= nx < N and 0 <= ny < M:
                # 다음 칸이 벽이 아니고, 아직 방문하지 않았다면
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))

                # 벽인데 아직 부수지 않았다면
                if graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    queue.append((nx, ny, 1))

    return -1  # 도달할 수 없음

# 입력 처리
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    print(bfs(N, M, graph))

if __name__ == "__main__":
    main()
