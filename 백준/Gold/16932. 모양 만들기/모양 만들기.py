import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 숫자 하나를 1로 변경해서 만들 수 있는 가장 큰 1의 덩어리 개수 구하기
    # 미리 각 모양을 탐색해두고, 0을 1로 바꿨을 때 인접한 모양들의 ID를 합쳐보자.
    group = dict() # group[id] = size
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def bfs(x, y, id):
        q = deque([(x, y)])
        size = 1
        board[x][y] = id
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1:
                    board[nx][ny] = id
                    size += 1
                    q.append((nx, ny))
        group[id] = size
    
    id = 2 # 2번부터
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(i, j, id)
                id += 1
    # 인접한 그룹끼리 연결했을 때 나올 수 있는 가장 큰 사이즈 구하기
    # 0을 기준으로 그룹 연결해보기
    max_size = 2 # 1은 하나 이상이라고 했으니까
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                group_set = set()
                for dx, dy in directions:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<n and 0<=ny<m and board[nx][ny] >= 2 and board[nx][ny] not in group_set: # id가 2부터 시작하니까
                        group_set.add((board[nx][ny]))
                size = 1 # board[x][y]를 1로 바꾸니까
                for g in group_set:
                    size += group[g]
                max_size = max(max_size, size)
    print(max_size)
solution()