import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 같은 x,y라도 검을 사용했는지 안 했는지에 따라 최단 거리가 달라진다.
    distance = [[[-1,-1] for _ in range(m)] for _ in range(n)] # 첫 방문인지 나타내기 위해서 -1로 초기화
    def bfs():
        # 0: 빈칸, 1: 벽, 2: 검
        q = deque([(0,0,0)]) # x, y, 검 사용 여부
        distance[0][0][0] = 0
        while q:
            x, y, sword  = q.popleft()
            
            if distance[x][y][sword] > t:
                print("Fail")
                return
            
            if x==n-1 and y==m-1:
                print(distance[x][y][sword])
                return
            
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if sword == 0:
                    if 0<=nx<n and 0<=ny<m and distance[nx][ny][sword] == -1 and board[nx][ny] != 1:
                        if board[nx][ny] == 0:
                            distance[nx][ny][sword] = distance[x][y][sword]+1                    
                            q.append((nx, ny, sword))
                        elif board[nx][ny] == 2:
                            distance[nx][ny][sword+1] = distance[x][y][sword]+1                    
                            q.append((nx, ny, sword+1))
                else:
                    if 0<=nx<n and 0<=ny<m and distance[nx][ny][sword] == -1:
                        distance[nx][ny][sword] = distance[x][y][sword]+1
                        q.append((nx, ny, sword))
        
        # 벽에 막혀 못 가면
        print("Fail")
        return
    bfs()
solution()