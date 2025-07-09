import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(n)]
    tetromino = [
        [(1,0),(2,0),(3,0)], [(0,1),(0,2),(0,3)], # 세로, 가로 일자
        [(0,1),(1,0),(1,1)], # 정사각형
        [(1,0),(2,0),(2,1)], [(1,0),(2,0),(2,-1)], [(-1,0),(-2,0),(-2,1)], [(-1,0),(-2,0),(-2,-1)], # ㄱ자 대칭
        [(0,1),(0,2),(1,2)], [(0,1),(0,2),(-1,2)], [(0,-1),(0,-2),(-1,-2)], [(0,-1),(0,-2),(1,-2)], # ㄱ자 회전
        [(1,0),(1,1),(2,1)], [(0,1),(-1,1),(-1,2)], [(-1,0),(-1,1),(-2,1)], [(0,1),(1,1),(1,2)], # S자 대칭과 회전 (중복 제거 중요!!)
        [(-1,0),(-1,-1),(-1,1)], [(1,0),(1,-1),(1,1)], [(0,1),(-1,1),(1,1)], [(0,-1),(-1,-1),(1,-1)] # 뻐큐
    ]
    def calculate(x, y, tet):
        score = s[x][y]
        for tx, ty in tet:
            nx, ny = tx+x, ty+y
            if 0<=nx<n and 0<=ny<m:
                score += s[nx][ny]
            else:
                return 0 # 범위에 벗어난다면 계산 바로 끝내야 한다.
        return score

    max_score = 0
    for i in range(n):
        for j in range(m):
            for tet in tetromino:
                score = calculate(i, j, tet)
                if score == 0:
                    continue
                max_score = max(max_score, score)
    print(max_score)
solution()