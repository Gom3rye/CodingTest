import sys
input = sys.stdin.readline
from itertools import combinations
def solution():
    n, m = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(n)]
    # T자 모양을 제외한 나머지 모양들은 backtracking으로 풀 수 있음

    biggestscrore = max(max(row) for row in s) # 가장 큰 점수
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    visited = [[False]*m for _ in range(n)]
    max_score = 0
    def backtracking(x, y, depth, score):
        nonlocal max_score, biggestscrore
        # 각 행의 가장 최고값을 더해도 max_score을 갱신할 수 없다면 넘어가자.
        if score + (4-depth)*biggestscrore < max_score:
            return
        if depth == 4:
            max_score = max(max_score, score)
            return
        
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                backtracking(nx, ny, depth+1, score+s[nx][ny])
                visited[nx][ny] = False

    def checkTshape(i, j):
        nonlocal max_score
        for tshape in combinations(directions, 3):
            tscore = s[i][j]
            for tx, ty in tshape:
                nx, ny = tx+i, ty+j
                if 0<=nx<n and 0<=ny<m:
                    tscore += s[nx][ny]
            max_score = max(max_score, tscore)

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            backtracking(i, j, 1, s[i][j])
            visited[i][j] = False # backtracking이 끝나고 나면 시작점도 False로 되돌려 놓기 때문에 if not visited[i][j]:가 없어도 된다.
    
            checkTshape(i, j)
    print(max_score)
solution()