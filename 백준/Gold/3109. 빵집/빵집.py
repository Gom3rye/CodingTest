import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [-1, 0, 1]  # 위, 중간, 아래
dy = [1, 1, 1]

visited = [[False]*C for _ in range(R)]

def dfs(x, y):
    if y == C - 1:
        return True
    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
    return False

answer = 0
for i in range(R):
    if board[i][0] == '.':
        visited[i][0] = True
        if dfs(i, 0):
            answer += 1

print(answer)
