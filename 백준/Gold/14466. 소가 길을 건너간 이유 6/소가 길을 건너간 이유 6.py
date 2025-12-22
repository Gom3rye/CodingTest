import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, k, r = map(int, input().split()) # 맵크기, #소, #길 <=100
    # 상0, 하1, 좌2, 우3
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 막힌 길부터 표시
    blocked = [[[False]*4 for _ in range(n)] for _ in range(n)] # [x][y][dir]: (x,y)에서 4방향의 길 있으니까
    for _ in range(r):
        # 모두 인접한 두 목초지를 잇는 길이다.
        r1, c1, r2, c2 = map(int, input().split())
        if r1 == r2:
            min_col = min(c1, c2) # c1을 더 작은 수로 고정
            max_col = max(c1, c2)
            blocked[r1-1][min_col-1][3] = True # 0based index
            blocked[r2-1][max_col-1][2] = True 
        else: # c1 == c2:
            min_row = min(r1, r2)
            max_row = max(r1, r2)
            blocked[min_row-1][c1-1][1] = True
            blocked[max_row-1][c2-1][0] = True
    
    cows = [list(map(int, input().split())) for _ in range(k)]
    # 소를 기준으로 bfs를 돌리면 시간초과 -> 땅을 기준으로 갈 수 있는 곳들을 그룹핑하자.
    ground = [[-1]*n for _ in range(n)]
    ground_idx = 0
    for i in range(n):
        for j in range(n):
            if ground[i][j] != -1: # 그룹핑 안 된 땅들만 bfs 돌려서 그룹핑!
                continue
            q = deque([(i, j)])
            ground[i][j] = ground_idx
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if not (0<=nx<n and 0<=ny<n):
                        continue
                    if blocked[x][y][d]: # 이 쪽으로 못가면 패쓰
                        continue
                    if ground[nx][ny] == -1: # visited 역할로 중복 방문 방지
                        ground[nx][ny] = ground_idx
                        q.append((nx, ny))
            ground_idx += 1
    
    cow_id = []
    for cx, cy in cows:
        # 0based index 잊지 말고!
        cow_id.append(ground[cx-1][cy-1]) # _번째 소는 이 인덱스 가지고 있게
    
    cnt = 0
    for i in range(k):
        for j in range(i+1, k):
            if cow_id[i] != cow_id[j]:
                cnt += 1

    print(cnt)
solution()