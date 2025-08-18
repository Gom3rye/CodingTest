import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    day = 0
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while True:
        visited = [[False]*n for _ in range(n)]
        q = deque()
        isavailable = False
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    union_score = 0
                    union = []
                    visited[i][j] = True
                    q.append((i, j))
                    union.append((i, j)) # 나중에 //하기 위해서
                    union_score += board[i][j] # 나중에 //하기 위해서
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = dx+x, dy+y
                            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(board[x][y]-board[nx][ny])<=r:
                                isavailable = True # 이동 가능함
                                visited[nx][ny] = True
                                union_score += board[nx][ny]
                                union.append((nx, ny))
                                q.append((nx, ny))

                # print(f"board: {board}")
                # print(f"union: {union}")
                for ux, uy in union:
                    board[ux][uy] = union_score // len(union)
                # print(f"board: {board}")
        # 이동 불가능하면 while문 나가서 day 출력
        if not isavailable:
            break
        
        day += 1

    print(day)                    
solution()