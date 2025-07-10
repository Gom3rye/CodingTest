import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(n)]
    biggestscrore = max(max(row) for row in s) # 가장 큰 점수
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    max_score = 0
    def backtracking(x, y, depth, score):
        nonlocal max_score, biggestscrore

        # 가장 최고 점수를 남은 횟수동안 더해도 max_score을 갱신할 수 없다면 넘어가자.
        if score + (4-depth)*biggestscrore < max_score:
            return
        
        if depth == 4:
            max_score = max(max_score, score)
            return

        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and s[nx][ny]: # 방문한 곳은 다 0으로 바꿔놨으니까 안 방문한 곳만 들어오도록(숫자가 있는 곳만)
                origin2 = s[nx][ny]
                if depth == 2: # T자 모양은 2번째 탐색 위치에서 상하좌우를 돌려야한다.(nx,ny로 돌리면 안됨)
                    s[nx][ny] = 0 # 방문 처리하고
                    backtracking(x, y, depth+1, score+origin2)
                    s[nx][ny] = origin2 # 원래 값 복원
                s[nx][ny] = 0
                backtracking(nx, ny, depth+1, score+origin2)
                s[nx][ny] = origin2

    for i in range(n):
        for j in range(m):
            origin1 = s[i][j]
            s[i][j] = 0 # 0으로 방문 처리하고
            backtracking(i, j, 1, origin1)
            s[i][j] = origin1 # backtracking이 끝나고 나면 시작점도 scr로 되돌려 놓기 때문에 if not s[i][j]:가 없어도 된다.
    print(max_score)
solution()