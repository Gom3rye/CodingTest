import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, t = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    # 짝수 초 -> all 0
    # 홀수 3, 7, 11
    #     5, 9, 13 # 원래 board
    def bfs(board):
        q = deque()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    q.append((i, j))
        visited = [[False]*m for i in range(n)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        board = [['O']*m for _ in range(n)]
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            board[x][y] = '.'
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 'O':
                    board[nx][ny] = '.'
                    visited[nx][ny] = True
        return board
    
    board3 = bfs(board)
    board5 = bfs(board3)
    
    if t == 1:
        for i in range(n):
            print("".join(board[i]))
        return

    elif t%2 == 0:
        board = ['O'*m]
        for i in range(n):
            print("".join(board))
        return
                
    elif t%4 == 3:
        for i in range(n):
            print("".join(board3[i]))
        return
    
    elif t%4 == 1:
        for i in range(n):
            print("".join(board5[i]))
        return
        
solution()