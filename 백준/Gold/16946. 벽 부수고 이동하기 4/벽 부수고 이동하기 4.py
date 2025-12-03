import sys
from collections import deque
input = sys.stdin.readline
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n, m = map(int, input().split()) # <=1000
    board = [list(map(int, input().strip())) for _ in range(n)]
    # n*m = 10^6이기 때문에 1있는 칸마다 bfs를 돌리는 건 10^12로 시간초과
    # 결국 중요한 건 이동할 수 있는 칸의 개수, 즉 0의 개수이므로 0끼리 그룹화해서 각 0영역에 대해 한번만 bfs를 돌리는 것으로 끝내야 한다.
    group_size = []
    group_id = [[-1]*m for _ in range(n)]
    def bfs(sx, sy, idx):
        q = deque([(sx, sy)])
        count = 1
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m and group_id[nx][ny] == -1 and not board[nx][ny]: # 0일때
                    group_id[nx][ny] = idx
                    count += 1
                    q.append((nx, ny))
        return count
    idx = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and group_id[i][j] == -1:
                group_id[i][j] = idx
                # idx가 0인 그룹에 대해 사이즈 구하기 (차례대로 1,2,3,4,...)
                group_size.append(bfs(i, j, idx))
                idx += 1

    # 0마다 group_id 붙이고 각 그룹의 size도 구했으니까 이제 1 방문하면서 정답 구하기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                adj_group_id = set()
                for dx, dy in directions:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<n and 0<=ny<m and group_id[nx][ny] != -1:
                        adj_group_id.add(group_id[nx][ny])
                
                for id in adj_group_id:
                    board[i][j] += group_size[id]
                board[i][j] %= 10
    # print(group_id)
    for row in board:
        print(*row, sep='')
solution()