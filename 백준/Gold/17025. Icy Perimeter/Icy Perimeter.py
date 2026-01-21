import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input()) # <=1000
    # perimeter 구하기 위해서 패딩값 주기
    temp = [list(input().strip()) for _ in range(n)]
    board = []
    board.append(['.']*(n+2))
    for i in range(n):
        board.append(['.']+temp[i]+['.'])
    board.append(['.']*(n+2))
    visited = [[False]*(n+2) for _ in range(n+2)]
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        cnt = 1
        perimeter = 0
        while q:
            x, y = q.popleft()
            for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if not (0<=nx<n+2 and 0<=ny<n+2):
                    continue
                if visited[nx][ny]:
                    continue

                if board[nx][ny] == '#':
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else: # perimeter 구해야 한다.
                    perimeter += 1

        return cnt, perimeter

    max_size = -1
    shortest_perimeter = float('inf')
    for i in range(n+2):
        for j in range(n+2):
            if board[i][j] == '#' and not visited[i][j]:
                size, perimeter = bfs(i, j)
                if size > max_size:
                    max_size = size
                    shortest_perimeter = perimeter
                elif size == max_size and shortest_perimeter > perimeter:
                    shortest_perimeter = perimeter
    print(max_size, shortest_perimeter)
solution()