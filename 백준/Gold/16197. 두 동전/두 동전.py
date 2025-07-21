import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    coins = [] # 두 동전의 좌표를 담는 리스트
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                coins.append((i, j))
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    # 벽이 아니면 무조건 이동할 수 있다.
    # coins의 길이가 1일때의 최단 거리
    def bfs(coins, count):
        q = deque()
        q.append((coins[0][0], coins[0][1], coins[1][0], coins[1][1], count))
        visited = {tuple(coins)}
        while q:
            x1, y1, x2, y2, count = q.popleft()
            if count >= 10:
                return -1

            for dx, dy in directions:
                nx1, ny1 = dx+x1, dy+y1
                nx2, ny2 = dx+x2, dy+y2

                fall1 = not (0<=nx1<n and 0<=ny1<m)
                fall2 = not (0<=nx2<n and 0<=ny2<m)

                if fall1 and fall2:
                    continue # 두 동전 모두 떨어진 경우 다음 방향 탐색
                if fall1 or fall2:
                    return count+1
                
                if board[nx1][ny1] == '#': # 벽이면 이동하지 않음
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2

                if (nx1, ny1, nx2, ny2) not in visited:
                    visited.add((nx1, ny1, nx2, ny2))
                    q.append((nx1, ny1, nx2, ny2, count+1))
        # while 끝날때까지 못 찾았으면 -1 
        return -1
    print(bfs(coins, 0))
solution()