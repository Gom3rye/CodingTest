import sys
input = sys.stdin.readline
from collections import deque
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    hdirections = [(-2,-1), (-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
    k = int(input())
    w, h = map(int, input().split()) # 가로, 세로
    board = [list(map(int, input().split())) for _ in range(h)]
    # dp[x][y][0]: 말처럼 이동 하지 않은 상태, dp[x][y][1]: 말처럼 이동한 상태
    def bfs():
        q = deque([(0,0,0)])
        # k번을 다 쓰고 최단 거리인지 안 쓰고 최단 거리인지 상태에 따라 다르다 -> 상태 추적해줘야 한다.
        dp = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]
        dp[0][0][0] = 0
        while q:
            x, y, count = q.popleft()
            if x ==(h-1) and y==(w-1):
                return dp[x][y][count]
            if count < k:
                for dx, dy in directions:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<h and 0<=ny<w and dp[nx][ny][count] == -1 and board[nx][ny] != 1:
                        dp[nx][ny][count] = dp[x][y][count] + 1 # 최단 거리 갱신
                        q.append((nx, ny, count))
                for dx, dy in hdirections:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<h and 0<=ny<w and dp[nx][ny][count+1] == -1 and board[nx][ny] != 1:
                        dp[nx][ny][count+1] = dp[x][y][count] + 1
                        q.append((nx, ny, count+1))
            else: # count == k: -> 더 이상 말 처럼 이동하면 안됨
                for dx, dy in directions:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<h and 0<=ny<w and dp[nx][ny][count] == -1 and board[nx][ny] != 1:
                        dp[nx][ny][count] = dp[x][y][count] + 1 # 최단 거리 갱신
                        q.append((nx, ny, count))
        return -1
    print(bfs())
solution()