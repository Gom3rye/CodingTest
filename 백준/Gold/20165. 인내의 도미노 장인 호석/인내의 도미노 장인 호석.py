import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 도미노 상태 저장용 따로 (공격 이후 수비 구현하기 위해서)
    fallen = [[False]*m for _ in range(n)]
    directions = {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}
    
    score = 0
    for _ in range(r):
        attx, atty, d = input().split()
        depx, depy = map(int, input().split())
        atx, aty = int(attx)-1, int(atty)-1 # 0based index
        dpx, dpy = depx-1, depy-1 # 0based index
        dx, dy = directions[d]
        q = deque([(atx, aty)])
        while q:
            x, y = q.popleft()
            target = board[x][y]
            if not fallen[x][y]:
                fallen[x][y] = True
                score += 1

            for i in range(1, target):
                nx, ny = dx*i+x, dy*i+y
                if 0<=nx<n and 0<=ny<m and not fallen[nx][ny]:
                    fallen[nx][ny] = True
                    score += 1
                    q.append((nx, ny))

        # 공격 끝 수비 차례
        if fallen[dpx][dpy]:
            fallen[dpx][dpy] = False
    
    print(score)
    for i in range(n):
        for j in range(m):
            print('F' if fallen[i][j] else 'S', end=' ')
        print()
                    
solution()