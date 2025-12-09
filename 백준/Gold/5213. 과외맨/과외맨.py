import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input()) # <=500
    board = []
    tiles = [[-1]*2*n for _ in range(n)]
    # board 채우고 tile idx 붙이기
    tile_idx = 1
    for i in range(n):
        row = []
        if i%2 == 0:
            j = 0
            for _ in range(n):
                # extend로 list합치기 +
                row.extend(list(map(int, input().split())))
                tiles[i][j] = tiles[i][j+1] = tile_idx
                tile_idx += 1
                j += 2
        else:
            j = 1
            for _ in range(n-1):
                row.extend(list(map(int, input().split())))
                tiles[i][j] = tiles[i][j+1] = tile_idx
                tile_idx += 1
                j += 2
            row = [0]+row+[0]
        board.append(row)

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    INF = float('inf')
    visited = [[INF]*(2*n) for _ in range(n)]
    visited[0][0] = 1

    prev = [[(-1, -1)]*2*n for _ in range(n)]
    prev[0][0] = 1
    
    max_tile, max_tile_loc = -1, (0, 0)
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        t = visited[x][y]

        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<2*n:
                # 같은 타일이어서 옆으로만 이동하는 것일때
                if tiles[nx][ny] == tiles[x][y] and t < visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = t
                    prev[nx][ny] = (x, y)
                    if max_tile < tiles[nx][ny]:
                        max_tile = tiles[nx][ny]
                        max_tile_loc = (nx, ny)
                
                else:
                    # 번호가 같게 붙어있을 때
                    if board[nx][ny] == board[x][y] and t+1 < visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = t+1
                        prev[nx][ny] = (x, y)
                        if max_tile < tiles[nx][ny]:
                            max_tile = tiles[nx][ny]
                            max_tile_loc = (nx, ny)
    
    def tracking(a, b):
        answer = [tiles[a][b]]
        x, y = prev[a][b]
        while (x, y) != (0, 0):
            if tiles[x][y] != answer[-1]:
                answer.append(tiles[x][y])
            x, y = prev[x][y]
        
        return answer[::-1]
    
    a, b = max_tile_loc
    answer = tracking(a, b)
    print(len(answer))
    print(*answer)
solution()