import sys
input = sys.stdin.readline
from collections import deque
def solution():
    w, h = map(int, input().split())
    # 외벽 판단을 위해 padding 값 주기
    board = [[0]*(w+2)] # top padding
    for _ in range(h):
        board.append([0]+list(map(int, input().split()))+[0])
    board.append([0]*(w+2)) # bottom padding
    # y가 홀수/짝수 인지에 따라 방향이 다르다. (y: width, x: height)
    # (y, x)
    odd_d = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]
    even_d = [(-1,-1),(0,-1),(1,0),(0,1),(-1,1),(-1,0)]
    dist = 0
    q = deque([(0,0)]) # (0,0)은 패딩값이므로 무조건 외벽
    visited = [[False]*(w+2) for _ in range(h+2)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        directions = odd_d if x%2 else even_d
        for dy, dx in directions:
            ny, nx = dy+y, dx+x
            if 0<=nx<h+2 and 0<=ny<w+2:
                if board[nx][ny] == 1: # 외벽에서 만난 건물
                    dist += 1
                elif not visited[nx][ny] and board[nx][ny] == 0: # 외벽 만났을 때는 방문 처리 해주고 q에 넣기
                    visited[nx][ny] = True
                    q.append((ny, nx))
    print(dist)             
solution()