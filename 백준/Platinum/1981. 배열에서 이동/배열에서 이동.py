import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

values = sorted(set(v for row in board for v in row))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_go(low, high):
    if not (low <= board[0][0] <= high):
        return False

    visited = [[False]*n for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and low <= board[nx][ny] <= high:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False

ans = float('inf')
l = 0

for r in range(len(values)):
    while l <= r and can_go(values[l], values[r]):
        ans = min(ans, values[r] - values[l])
        l += 1

print(ans)