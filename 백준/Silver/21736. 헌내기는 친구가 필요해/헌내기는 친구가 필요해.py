import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    campus = [list(input().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    # 도연이 위치 찾기
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                start = (i, j)
                break

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([start])
    visited[start[0]][start[1]] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and campus[nx][ny] != 'X':
                    visited[nx][ny] = True
                    if campus[nx][ny] == 'P':
                        count += 1
                    queue.append((nx, ny))
    
    print(count if count > 0 else "TT")

solution()