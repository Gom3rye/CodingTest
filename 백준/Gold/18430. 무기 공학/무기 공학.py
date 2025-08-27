import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_score = 0
    boomerangs = [[(0,0),(0,1),(1,0)],
                  [(0,0),(0,-1),(1,0)],
                  [(0,0),(-1,0),(0,1)],
                  [(0,0),(-1,0),(0,-1)]
    ]
    visited = [[False]*m for _ in range(n)]

    def backtracking(idx, score):
        nonlocal max_score
        if idx == n*m:
            max_score = max(max_score, score)
            return
        # 2중 for문으로 만들면 검사 완료한 곳도 다시 봐야 하니까 2차원배열 flatten 해서 idx로 검사
        x, y = idx//m, idx%m

        if not visited[x][y]:
            for shape in boomerangs:
                can_make = True
                cells = []
                for dx, dy in shape:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                        cells.append((nx, ny))
                    else:
                        can_make = False
                        break
                # 부메랑을 하나 놓을 수 있는 경우
                if can_make:
                    values = 0
                    for i, (cx, cy) in enumerate(cells):
                        visited[cx][cy] = True
                        if i == 0:
                            values += board[cx][cy]*2
                        else:
                            values += board[cx][cy]
                    backtracking(idx+1, score+values)
                    # 상태 복구
                    for cx, cy in cells:
                        visited[cx][cy] = False
        
        # 현재 칸 놓지 않는 경우도 고려
        backtracking(idx+1, score)

    backtracking(0, 0)
    print(max_score)
solution()