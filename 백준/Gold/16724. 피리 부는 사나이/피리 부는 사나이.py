import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    directions = {'D': (1,0), 'L': (0,-1), 'R': (0,1), 'U': (-1,0)}
    # 사이클의 개수 = safe zone의 최소 개수
    visited = [[-1]*m for _ in range(n)] # -1: 미방문, 1: 방문 중, 2: 방문 완료
    count = 0
    def dfs(x, y):
        nonlocal count
        # 방문 중으로 표시
        visited[x][y] = 1
        d = board[x][y]
        dx, dy = directions[d]
        nx, ny = dx+x, dy+y
        if visited[nx][ny] == 1: # 사이클 만남
            count += 1 # save zone 표시
        elif visited[nx][ny] == -1:
            dfs(nx, ny)

        visited[x][y] = 2
        return
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1:
                dfs(i, j)
    print(count)
solution()